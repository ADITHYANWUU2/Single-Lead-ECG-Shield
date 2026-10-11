/*
  ==============================================================================
  Project: Single-Lead ECG Shield for Arduino
  Description: Real-time Electrocardiogram (ECG) acquisition, Leads-Off Detection,
               R-Peak QRS detection, and BPM calculation with Serial Plotter output.
  Target Hardware: Arduino Uno / Mega / Nano / Leonardo + Single-Lead ECG Shield
  Analog Front End: Analog Devices AD8232 (Gain: 1100 V/V, Bandpass: 0.5Hz - 40Hz)
  Author: ADITHYANWUU2 (Open Source Hardware Lab)
  License: MIT License
  ==============================================================================
*/

// Pin Assignments
const int PIN_ECG_IN      = A0;  // Analog ECG input from Shield
const int PIN_LOD_PLUS    = 10;  // Leads-Off Detection Positive (+IN detached)
const int PIN_LOD_MINUS   = 11;  // Leads-Off Detection Negative (-IN detached)
const int PIN_FAST_RESTORE= 9;   // Fast Restore trigger (pulses high to reset HPF)
const int PIN_SHUTDOWN    = 8;   // Active-low shutdown control (HIGH = Enabled)
const int PIN_BEAT_LED    = 13;  // Onboard Arduino LED for heartbeat pulse

// Sampling & Timing Configuration
const unsigned long SAMPLE_INTERVAL_US = 4000; // 250 Hz sampling rate (4ms interval)
unsigned long lastSampleTime = 0;

// QRS Detection & BPM Variables
int ecgRaw = 0;
int ecgFiltered = 0;
int prevSample = 0;
int derivative = 0;
int threshold = 30; // Adaptive threshold baseline
unsigned long lastPeakTime = 0;
float currentBPM = 0.0;
bool peakDetected = false;

// Moving average buffer for baseline smoothing
const int FILTER_SIZE = 5;
int filterBuffer[FILTER_SIZE];
int filterIdx = 0;

void setup() {
  Serial.begin(115200);
  while (!Serial && millis() < 3000); // Wait for serial console (Leonardo/Micro)

  // Configure digital GPIOs
  pinMode(PIN_LOD_PLUS, INPUT);
  pinMode(PIN_LOD_MINUS, INPUT);
  pinMode(PIN_FAST_RESTORE, OUTPUT);
  pinMode(PIN_SHUTDOWN, OUTPUT);
  pinMode(PIN_BEAT_LED, OUTPUT);

  // Initialize AD8232 in active operating state
  digitalWrite(PIN_SHUTDOWN, HIGH);    // Enable AD8232
  digitalWrite(PIN_FAST_RESTORE, LOW); // Normal filter recovery mode
  digitalWrite(PIN_BEAT_LED, LOW);

  // Pulse Fast Restore during startup to rapidly settle high-pass filter caps
  triggerFastRestore();

  // Print header for Arduino Serial Plotter
  Serial.println("ECG_Raw,Threshold,BPM_Indicator,Leads_Connected");
}

void loop() {
  unsigned long currentMicros = micros();

  // Enforce consistent 250 Hz sampling rate
  if (currentMicros - lastSampleTime >= SAMPLE_INTERVAL_US) {
    lastSampleTime = currentMicros;

    // Check Leads-Off Condition
    bool leadsOff = (digitalRead(PIN_LOD_PLUS) == HIGH) || (digitalRead(PIN_LOD_MINUS) == HIGH);

    if (leadsOff) {
      // Electrode patch fell off or loose skin contact
      digitalWrite(PIN_BEAT_LED, LOW);
      currentBPM = 0;
      
      // Output flatline and status to Serial Plotter
      Serial.print(512); // Virtual center line (1.65V)
      Serial.print(" ");
      Serial.print(512);
      Serial.print(" ");
      Serial.print(0);
      Serial.print(" ");
      Serial.println(0); // 0 = Disconnected
      return;
    }

    // Read analog ECG signal (0 to 1023 ADC counts, ~3.22mV/count at 3.3V)
    ecgRaw = analogRead(PIN_ECG_IN);

    // Simple moving average low-pass filter to reject any residual 50/60Hz hash
    filterBuffer[filterIdx] = ecgRaw;
    filterIdx = (filterIdx + 1) % FILTER_SIZE;
    long sum = 0;
    for (int i = 0; i < FILTER_SIZE; i++) {
      sum += filterBuffer[i];
    }
    ecgFiltered = sum / FILTER_SIZE;

    // Calculate first-derivative (slope of QRS complex)
    derivative = abs(ecgFiltered - prevSample);
    prevSample = ecgFiltered;

    // Real-Time QRS Detection Logic
    unsigned long now = millis();
    if (derivative > threshold && (now - lastPeakTime > 300)) { // 300ms refractory period (max 200 BPM)
      // R-Peak detected!
      unsigned long rrInterval = now - lastPeakTime;
      lastPeakTime = now;

      if (rrInterval > 300 && rrInterval < 2000) {
        float instantBPM = 60000.0 / (float)rrInterval;
        // Smooth BPM using exponential moving average
        currentBPM = (currentBPM == 0) ? instantBPM : (currentBPM * 0.7 + instantBPM * 0.3);
      }

      peakDetected = true;
      digitalWrite(PIN_BEAT_LED, HIGH);
      
      // Adaptively update detection threshold
      threshold = (threshold * 0.6) + (derivative * 0.4);
    } else {
      peakDetected = false;
      // Decay threshold slowly toward baseline
      if (threshold > 25) {
        threshold -= 1;
      }
      digitalWrite(PIN_BEAT_LED, LOW);
    }

    // Print values formatted for Arduino IDE Serial Plotter
    Serial.print(ecgFiltered);
    Serial.print(" ");
    Serial.print(512 + threshold * 2);
    Serial.print(" ");
    Serial.print(peakDetected ? 750 : 512);
    Serial.print(" ");
    Serial.println(1000); // 1000 = Connected & active
  }
}

// Rapidly discharges input high-pass filter capacitors for instant signal recovery
void triggerFastRestore() {
  digitalWrite(PIN_FAST_RESTORE, HIGH);
  delay(50);
  digitalWrite(PIN_FAST_RESTORE, LOW);
}
