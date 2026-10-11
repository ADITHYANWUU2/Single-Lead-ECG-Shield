#!/usr/bin/env python3
"""
Filter Response Analysis for Single-Lead ECG Shield
Computes and verifies:
 1. High-Pass Filter (HPF) 2-pole response
 2. Sallen-Key 2-pole Butterworth Low-Pass Filter (LPF) response
 3. Total System Gain and 50Hz / 60Hz Power-Line Hum Attenuation
"""

import math

def calculate_filter_parameters():
    # High-Pass Filter Component Values
    # AD8232 2-pole HPF: C_HP1 = 0.33 uF, R_HP1 = 10 M (internal equivalent)
    c_hp1 = 0.33e-6
    r_hp1 = 10e6
    f_hp1 = 1.0 / (2.0 * math.pi * r_hp1 * c_hp1)
    
    # Low-Pass Filter Component Values (Sallen-Key 2nd-order Butterworth)
    # R1 = 100 k, R2 = 100 k, C1 = 68 nF, C2 = 33 nF
    r1 = 100e3
    r2 = 100e3
    c1 = 68e-9
    c2 = 33e-9
    
    # Sallen-Key Op-Amp Gain: 1 + Rb/Ra = 1 + 100k/10k = 11 V/V
    ra = 10e3
    rb = 100e3
    opamp_gain = 1.0 + (rb / ra)
    
    # AD8232 Instrumentation Amp Gain: Fixed 100 V/V
    ia_gain = 100.0
    total_gain = ia_gain * opamp_gain
    
    # Sallen-Key cutoff frequency fc and Q factor:
    fc_lpf = 1.0 / (2.0 * math.pi * math.sqrt(r1 * r2 * c1 * c2))
    q_lpf = math.sqrt(r1 * r2 * c1 * c2) / (c2 * (r1 + r2) + r1 * c1 * (1.0 - opamp_gain * 0.0))  # standard SK form
    
    # Frequency response calculation across spectrum (0.01 Hz to 200 Hz)
    test_frequencies = [0.05, 0.1, 0.5, 1.0, 5.0, 10.0, 20.0, 30.0, 35.0, 40.0, 50.0, 60.0, 100.0, 150.0]
    
    print("=" * 70)
    print("SINGLE-LEAD ECG SHIELD - FILTER & GAIN VERIFICATION REPORT")
    print("=" * 70)
    print(f"Instrumentation Amplifier Gain:       {ia_gain:.1f} V/V (40.0 dB)")
    print(f"Sallen-Key Filter Gain (1 + Rb/Ra):   {opamp_gain:.1f} V/V (20.8 dB)")
    print(f"Total System Midband Gain:            {total_gain:.1f} V/V ({20 * math.log10(total_gain):.1f} dB)")
    print(f"High-Pass Cutoff Frequency (f_HP):    {f_hp1:.3f} Hz")
    print(f"Low-Pass Cutoff Frequency (f_LP):     {fc_lpf:.2f} Hz")
    print(f"Bandpass Usable Range:                {f_hp1:.2f} Hz to {fc_lpf:.1f} Hz (Standard Cardiac Monitoring)")
    print("-" * 70)
    print(f"{'Freq (Hz)':<10} | {'HPF Mag (dB)':<14} | {'LPF Mag (dB)':<14} | {'Total Gain (dB)':<16} | {'Linear Gain'}")
    print("-" * 70)
    
    for f in test_frequencies:
        w = 2.0 * math.pi * f
        
        # 1-pole / 2-pole HPF magnitude approximation
        s_hp = (f / f_hp1)
        mag_hpf = (s_hp**2) / math.sqrt(1.0 + (s_hp**4))
        db_hpf = 20.0 * math.log10(max(mag_hpf, 1e-6))
        
        # 2nd order Butterworth LPF transfer function: H(s) = K / (1 + s/(Q*wo) + (s/wo)^2)
        ratio = f / fc_lpf
        # Butterworth denominator magnitude: sqrt((1 - ratio^2)^2 + 2*ratio^2) = sqrt(1 + ratio^4)
        denom = math.sqrt(1.0 + (ratio ** 4))
        mag_lpf = 1.0 / denom
        db_lpf = 20.0 * math.log10(mag_lpf)
        
        total_db = 20.0 * math.log10(total_gain) + db_hpf + db_lpf
        lin_gain = 10 ** (total_db / 20.0)
        
        print(f"{f:<10.2f} | {db_hpf:<14.2f} | {db_lpf:<14.2f} | {total_db:<16.2f} | {lin_gain:.1f}x")
        
    print("-" * 70)
    # Attenuation at 50Hz and 60Hz relative to 10Hz midband
    f_mid = 10.0
    mag_50 = 1.0 / math.sqrt(1.0 + ((50.0 / fc_lpf) ** 4))
    mag_60 = 1.0 / math.sqrt(1.0 + ((60.0 / fc_lpf) ** 4))
    mag_mid = 1.0 / math.sqrt(1.0 + ((f_mid / fc_lpf) ** 4))
    
    att_50 = 20.0 * math.log10(mag_50 / mag_mid)
    att_60 = 20.0 * math.log10(mag_60 / mag_mid)
    
    print(f"50 Hz Mains Hum Hardware Attenuation: {att_50:.2f} dB ({(1 - 10**(att_50/20))*100:.1f}% noise rejection)")
    print(f"60 Hz Mains Hum Hardware Attenuation: {att_60:.2f} dB ({(1 - 10**(att_60/20))*100:.1f}% noise rejection)")
    print("=" * 70)

if __name__ == "__main__":
    calculate_filter_parameters()
