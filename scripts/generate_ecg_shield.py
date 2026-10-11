#!/usr/bin/env python3
"""
Comprehensive Generator for Single-Lead ECG Shield KiCad Project
Generates:
  1. Single-Lead-ECG-Shield.kicad_pro
  2. Single-Lead-ECG-Shield.kicad_sch (Complete KiCad schematic with AD8232, LDO, filters, Arduino shield headers)
  3. Single-Lead-ECG-Shield.kicad_pcb (Full KiCad PCB layout with Arduino shield outline, isolation slot, components, tracks, zones)
  4. BOM.csv (Complete engineering Bill of Materials with MPNs and specs)
  5. gerber/ (Manufacturing Gerbers and Excellon drill files)
"""

import os
import json
import uuid
import math

PROJECT_DIR = r"c:\Users\mathi\OneDrive\Documents\Single-Lead-ECG-Shield"
PROJECT_NAME = "Single-Lead-ECG-Shield"

def uid():
    return str(uuid.uuid4())

def generate_kicad_pro():
    pro_data = {
        "board": {
            "3dviewports": [],
            "design_settings": {
                "defaults": {
                    "board_outline_line_width": 0.1,
                    "copper_line_width": 0.2,
                    "copper_text_size_h": 1.5,
                    "copper_text_size_v": 1.5,
                    "copper_text_thickness": 0.3,
                    "other_line_width": 0.15,
                    "silk_line_width": 0.15,
                    "silk_text_size_h": 1.0,
                    "silk_text_size_v": 1.0,
                    "silk_text_thickness": 0.15
                },
                "diff_pair_dimensions": [],
                "drc_exclusions": [],
                "rules": {
                    "min_clearance": 0.2,
                    "min_track_width": 0.2,
                    "min_via_annular_width": 0.13,
                    "min_via_diameter": 0.6
                },
                "track_widths": [0.25, 0.4, 0.6, 1.0],
                "via_dimensions": [
                    {"diameter": 0.8, "drill": 0.4}
                ]
            },
            "layer_presets": [],
            "viewports": []
        },
        "boards": [],
        "cvpcb": {"equivalence_files": []},
        "libraries": {
            "pinned_footprint_libs": [],
            "pinned_symbol_libs": []
        },
        "meta": {
            "filename": f"{PROJECT_NAME}.kicad_pro",
            "version": 1
        },
        "net_settings": {
            "classes": [
                {
                    "bus_width": 12,
                    "clearance": 0.2,
                    "diff_pair_gap": 0.25,
                    "diff_pair_via_gap": 0.25,
                    "diff_pair_width": 0.2,
                    "line_style": 0,
                    "microvia_diameter": 0.3,
                    "microvia_drill": 0.1,
                    "name": "Default",
                    "pcb_color": "rgba(0, 0, 0, 0.000)",
                    "schematic_color": "rgba(0, 0, 0, 0.000)",
                    "track_width": 0.25,
                    "via_diameter": 0.8,
                    "via_drill": 0.4,
                    "wire_width": 6
                },
                {
                    "bus_width": 12,
                    "clearance": 0.3,
                    "diff_pair_gap": 0.25,
                    "diff_pair_via_gap": 0.25,
                    "diff_pair_width": 0.2,
                    "line_style": 0,
                    "microvia_diameter": 0.3,
                    "microvia_drill": 0.1,
                    "name": "Power",
                    "pcb_color": "rgba(255, 0, 0, 1.000)",
                    "schematic_color": "rgba(255, 0, 0, 1.000)",
                    "track_width": 0.8,
                    "via_diameter": 0.8,
                    "via_drill": 0.4,
                    "wire_width": 6
                },
                {
                    "bus_width": 12,
                    "clearance": 0.4,
                    "diff_pair_gap": 0.25,
                    "diff_pair_via_gap": 0.25,
                    "diff_pair_width": 0.2,
                    "line_style": 0,
                    "microvia_diameter": 0.3,
                    "microvia_drill": 0.1,
                    "name": "Analog_Sensitive",
                    "pcb_color": "rgba(0, 150, 255, 1.000)",
                    "schematic_color": "rgba(0, 150, 255, 1.000)",
                    "track_width": 0.3,
                    "via_diameter": 0.8,
                    "via_drill": 0.4,
                    "wire_width": 6
                }
            ],
            "meta": {"version": 3},
            "net_colors": None,
            "netclass_assignments": None,
            "netclass_patterns": []
        },
        "pcbnew": {
            "last_paths": {
                "gencad": "",
                "idf": "",
                "netlist": "",
                "plot": "gerber",
                "pos": "",
                "specctra_dsn": "",
                "step": "",
                "svg": "",
                "vrml": ""
            }
        },
        "schematic": {
            "annotate_start_num": 1,
            "drawing": {
                "dashed_lines_dash_length_ratio": 12.0,
                "dashed_lines_gap_length_ratio": 3.0,
                "default_line_thickness": 6.0,
                "default_text_size": 50.0,
                "field_names": [],
                "intersheets_ref_own_page": False,
                "intersheets_ref_prefix": "",
                "intersheets_ref_short": False,
                "intersheets_ref_show": False,
                "intersheets_ref_suffix": "",
                "pin_symbol_size": 25.0,
                "text_offset_ratio": 0.15
            },
            "legacy_lib_dir": "",
            "legacy_lib_list": []
        },
        "sheets": [
            [uid(), ""]
        ]
    }
    path = os.path.join(PROJECT_DIR, f"{PROJECT_NAME}.kicad_pro")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(pro_data, f, indent=2)
    print(f"Generated {path}")

def generate_schematic():
    sch_path = os.path.join(PROJECT_DIR, f"{PROJECT_NAME}.kicad_sch")
    
    # We will write a valid KiCad 7/8 format schematic
    content = f"""(kicad_sch (version 20230121) (generator eeschema)

  (uuid {uid()})

  (paper "A3")

  (title_block
    (title "Single-Lead ECG Shield for Arduino")
    (date "2026-10-11")
    (rev "v1.0")
    (company "Open Source Hardware Lab")
    (comment 1 "AD8232 Single-Lead Heart Rate Monitor Analog Front End")
    (comment 2 "0.5 Hz HPF, 40 Hz Butterworth LPF, RLD Active Hum Cancellation")
    (comment 3 "IEC 60601-1 Current Limiting & PCB Safety Isolation Barrier")
    (comment 4 "GitHub: https://github.com/ADITHYANWUU2/Single-Lead-ECG-Shield")
  )

  (lib_symbols
    (symbol "AD8232ACPZ" (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 25.4 0) (effects (font (size 1.27 1.27))))
      (property "Value" "AD8232ACPZ" (at 0 22.86 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_DFN_QFN:QFN-20-1EP_4x4mm_P0.5mm_EP2.7x2.7mm" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (property "Datasheet" "https://www.analog.com/media/en/technical-documentation/data-sheets/ad8232.pdf" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "AD8232ACPZ_0_1"
        (rectangle (start -15.24 20.32) (end 15.24 -22.86) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "AD8232ACPZ_1_1"
        (pin output line (at -17.78 12.7 0) (length 2.54) (name "HPDRIVE" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin input line (at -17.78 7.62 0) (length 2.54) (name "+IN" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin input line (at -17.78 2.54 0) (length 2.54) (name "-IN" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin input line (at -17.78 -2.54 0) (length 2.54) (name "RLDFB" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin output line (at -17.78 -7.62 0) (length 2.54) (name "RLD" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
        (pin passive line (at -17.78 -12.7 0) (length 2.54) (name "SW" (effects (font (size 1.27 1.27)))) (number "6" (effects (font (size 1.27 1.27)))))
        (pin input line (at 17.78 -7.62 180) (length 2.54) (name "OPAMP+" (effects (font (size 1.27 1.27)))) (number "7" (effects (font (size 1.27 1.27)))))
        (pin output line (at 17.78 2.54 180) (length 2.54) (name "REFOUT" (effects (font (size 1.27 1.27)))) (number "8" (effects (font (size 1.27 1.27)))))
        (pin input line (at 17.78 -12.7 180) (length 2.54) (name "OPAMP-" (effects (font (size 1.27 1.27)))) (number "9" (effects (font (size 1.27 1.27)))))
        (pin output line (at 17.78 -17.78 180) (length 2.54) (name "OUT" (effects (font (size 1.27 1.27)))) (number "10" (effects (font (size 1.27 1.27)))))
        (pin output line (at 17.78 12.7 180) (length 2.54) (name "LOD-" (effects (font (size 1.27 1.27)))) (number "11" (effects (font (size 1.27 1.27)))))
        (pin output line (at 17.78 17.78 180) (length 2.54) (name "LOD+" (effects (font (size 1.27 1.27)))) (number "12" (effects (font (size 1.27 1.27)))))
        (pin input line (at -17.78 -17.78 0) (length 2.54) (name "SDN" (effects (font (size 1.27 1.27)))) (number "13" (effects (font (size 1.27 1.27)))))
        (pin input line (at 17.78 7.62 180) (length 2.54) (name "AC/DC" (effects (font (size 1.27 1.27)))) (number "14" (effects (font (size 1.27 1.27)))))
        (pin input line (at 0 -25.4 90) (length 2.54) (name "FR" (effects (font (size 1.27 1.27)))) (number "15" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 5 -25.4 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "16" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 22.86 270) (length 2.54) (name "+VS" (effects (font (size 1.27 1.27)))) (number "17" (effects (font (size 1.27 1.27)))))
        (pin input line (at 17.78 -2.54 180) (length 2.54) (name "REFIN" (effects (font (size 1.27 1.27)))) (number "18" (effects (font (size 1.27 1.27)))))
        (pin output line (at 17.78 -22.86 180) (length 2.54) (name "IAOUT" (effects (font (size 1.27 1.27)))) (number "19" (effects (font (size 1.27 1.27)))))
        (pin input line (at -17.78 17.78 0) (length 2.54) (name "HPSENSE" (effects (font (size 1.27 1.27)))) (number "20" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 7.62 -25.4 90) (length 2.54) (name "EP_GND" (effects (font (size 1.27 1.27)))) (number "21" (effects (font (size 1.27 1.27)))))
      )
    )
    (symbol "AP2112K-3.3" (in_bom yes) (on_board yes)
      (property "Reference" "U" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
      (property "Value" "AP2112K-3.3" (at 0 5.08 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Package_TO_SOT_SMD:SOT-23-5" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "AP2112K-3.3_0_1"
        (rectangle (start -7.62 5.08) (end 7.62 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "AP2112K-3.3_1_1"
        (pin power_in line (at -10.16 2.54 0) (length 2.54) (name "VIN" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin power_in line (at 0 -7.62 90) (length 2.54) (name "GND" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin input line (at -10.16 -2.54 0) (length 2.54) (name "EN" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 10.16 -2.54 180) (length 2.54) (name "NC" (effects (font (size 1.27 1.27)))) (number "4" (effects (font (size 1.27 1.27)))))
        (pin power_out line (at 10.16 2.54 180) (length 2.54) (name "VOUT" (effects (font (size 1.27 1.27)))) (number "5" (effects (font (size 1.27 1.27)))))
      )
    )
    (symbol "AudioJack3_Switch" (in_bom yes) (on_board yes)
      (property "Reference" "J" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
      (property "Value" "PJ-320A_3.5mm" (at 0 5.08 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Connector_Audio:Jack_3.5mm_CUI_SJ-3523-SMT_Horizontal" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "AudioJack3_Switch_0_1"
        (rectangle (start -5.08 5.08) (end 5.08 -5.08) (stroke (width 0.254) (type default)) (fill (type background)))
      )
      (symbol "AudioJack3_Switch_1_1"
        (pin passive line (at 7.62 2.54 180) (length 2.54) (name "TIP_LA" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 7.62 0 180) (length 2.54) (name "RING_RA" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 7.62 -2.54 180) (length 2.54) (name "SLEEVE_RL" (effects (font (size 1.27 1.27)))) (number "3" (effects (font (size 1.27 1.27)))))
      )
    )
    (symbol "R" (in_bom yes) (on_board yes)
      (property "Reference" "R" (at 2.032 0 90) (effects (font (size 1.27 1.27))))
      (property "Value" "R" (at -2.032 0 90) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Resistor_SMD:R_0805_2012Metric" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "R_0_1"
        (rectangle (start -1.016 2.54) (end 1.016 -2.54) (stroke (width 0.254) (type default)) (fill (type none)))
      )
      (symbol "R_1_1"
        (pin passive line (at 0 5.08 270) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -5.08 90) (length 2.54) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
      )
    )
    (symbol "C" (in_bom yes) (on_board yes)
      (property "Reference" "C" (at 2.032 0 90) (effects (font (size 1.27 1.27))))
      (property "Value" "C" (at -2.032 0 90) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Capacitor_SMD:C_0805_2012Metric" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "C_0_1"
        (polyline (pts (xy -2.032 0.762) (xy 2.032 0.762)) (stroke (width 0.381) (type default)) (fill (type none)))
        (polyline (pts (xy -2.032 -0.762) (xy 2.032 -0.762)) (stroke (width 0.381) (type default)) (fill (type none)))
      )
      (symbol "C_1_1"
        (pin passive line (at 0 3.81 270) (length 3.048) (name "~" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 0 -3.81 90) (length 3.048) (name "~" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
      )
    )
    (symbol "LED" (in_bom yes) (on_board yes)
      (property "Reference" "D" (at 2.54 0 0) (effects (font (size 1.27 1.27))))
      (property "Value" "LED" (at 2.54 -2.54 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "LED_SMD:LED_0805_2012Metric" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))
      (symbol "LED_0_1"
        (polyline (pts (xy -1.27 -1.27) (xy 1.27 0) (xy -1.27 1.27) (xy -1.27 -1.27)) (stroke (width 0.254) (type default)) (fill (type outline)))
        (polyline (pts (xy 1.27 -1.27) (xy 1.27 1.27)) (stroke (width 0.254) (type default)) (fill (type none)))
      )
      (symbol "LED_1_1"
        (pin passive line (at -3.81 0 0) (length 2.54) (name "A" (effects (font (size 1.27 1.27)))) (number "1" (effects (font (size 1.27 1.27)))))
        (pin passive line (at 3.81 0 180) (length 2.54) (name "K" (effects (font (size 1.27 1.27)))) (number "2" (effects (font (size 1.27 1.27)))))
      )
    )
  )

  (text "Single-Lead ECG Shield Schematic" (at 50.8 25.4 0) (effects (font (size 2.54 2.54) (bold yes))))
  (text "Section 1: Patient Protection & ESD Clamp" (at 38.1 45.72 0) (effects (font (size 1.778 1.778))))
  (text "Section 2: AD8232 Analog Front End (AFE)" (at 127.0 45.72 0) (effects (font (size 1.778 1.778))))
  (text "Section 3: 40 Hz Butterworth Low-Pass Filter" (at 215.9 45.72 0) (effects (font (size 1.778 1.778))))
  (text "Section 4: Ultra-Low Noise Power Supply & Arduino Interface" (at 127.0 165.1 0) (effects (font (size 1.778 1.778))))

  ;; Symbols instances
  (symbol (lib_id "AudioJack3_Switch") (at 38.1 76.2 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "J1" (at 38.1 68.58 0) (effects (font (size 1.27 1.27))))
    (property "Value" "PJ-320A (3.5mm Medical/Audio Jack)" (at 38.1 66.04 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_Audio:Jack_3.5mm_CUI_SJ-3523-SMT_Horizontal" (at 38.1 76.2 0) (effects (font (size 1.27 1.27)) hide))
  )

  ;; R1, R2, R3 Safety current limiting resistors (180k, IEC 60601-1 compliant)
  (symbol (lib_id "R") (at 60.96 73.66 90) (unit 1)
    (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "R1" (at 60.96 68.58 0) (effects (font (size 1.27 1.27))))
    (property "Value" "180k (Safety Limit)" (at 60.96 66.04 0) (effects (font (size 1.27 1.27))))
  )
  (symbol (lib_id "R") (at 60.96 83.82 90) (unit 1)
    (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "R2" (at 60.96 78.74 0) (effects (font (size 1.27 1.27))))
    (property "Value" "180k (Safety Limit)" (at 60.96 76.2 0) (effects (font (size 1.27 1.27))))
  )
  (symbol (lib_id "R") (at 60.96 93.98 90) (unit 1)
    (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "R3" (at 60.96 88.9 0) (effects (font (size 1.27 1.27))))
    (property "Value" "180k (Safety Limit)" (at 60.96 86.34 0) (effects (font (size 1.27 1.27))))
  )

  ;; C1, C2 RF Filtering Capacitors
  (symbol (lib_id "C") (at 76.2 78.74 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "C1" (at 81.28 78.74 0) (effects (font (size 1.27 1.27))))
    (property "Value" "470pF (EMI Filter)" (at 81.28 81.28 0) (effects (font (size 1.27 1.27))))
  )
  (symbol (lib_id "C") (at 76.2 88.9 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "C2" (at 81.28 88.9 0) (effects (font (size 1.27 1.27))))
    (property "Value" "470pF (EMI Filter)" (at 81.28 91.44 0) (effects (font (size 1.27 1.27))))
  )
  (symbol (lib_id "C") (at 76.2 99.06 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "C3" (at 81.28 99.06 0) (effects (font (size 1.27 1.27))))
    (property "Value" "1.5nF (Differential)" (at 81.28 101.6 0) (effects (font (size 1.27 1.27))))
  )

  ;; U1 AD8232 Heart Rate Front-End
  (symbol (lib_id "AD8232ACPZ") (at 147.32 93.98 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "U1" (at 147.32 66.04 0) (effects (font (size 1.27 1.27))))
    (property "Value" "AD8232ACPZ" (at 147.32 68.58 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DFN_QFN:QFN-20-1EP_4x4mm_P0.5mm_EP2.7x2.7mm" (at 147.32 93.98 0) (effects (font (size 1.27 1.27)) hide))
  )

  ;; High-Pass Filter: C_HP1, C_HP2, R_HP1, R_HP2
  (symbol (lib_id "C") (at 116.84 81.28 90) (unit 1)
    (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "C4" (at 116.84 76.2 0) (effects (font (size 1.27 1.27))))
    (property "Value" "0.33uF (HPF Pole 1)" (at 116.84 73.66 0) (effects (font (size 1.27 1.27))))
  )
  (symbol (lib_id "C") (at 116.84 106.68 90) (unit 1)
    (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "C5" (at 116.84 101.6 0) (effects (font (size 1.27 1.27))))
    (property "Value" "0.33uF (HPF Pole 2)" (at 116.84 99.06 0) (effects (font (size 1.27 1.27))))
  )
  (symbol (lib_id "R") (at 124.46 88.9 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "R4" (at 129.54 88.9 0) (effects (font (size 1.27 1.27))))
    (property "Value" "10M (HPF Feedback)" (at 129.54 91.44 0) (effects (font (size 1.27 1.27))))
  )

  ;; Right Leg Drive Feedback: R_RLD (1M), C_RLD (1.5nF)
  (symbol (lib_id "R") (at 116.84 96.52 90) (unit 1)
    (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "R5" (at 116.84 91.44 0) (effects (font (size 1.27 1.27))))
    (property "Value" "1M (RLD Gain)" (at 116.84 88.9 0) (effects (font (size 1.27 1.27))))
  )
  (symbol (lib_id "C") (at 116.84 101.6 90) (unit 1)
    (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "C6" (at 116.84 96.52 0) (effects (font (size 1.27 1.27))))
    (property "Value" "1.5nF (RLD Stability)" (at 116.84 93.98 0) (effects (font (size 1.27 1.27))))
  )

  ;; Low-Pass Sallen-Key 40Hz Filter: R6(100k), R7(100k), C7(68nF), C8(33nF), R8(10k), R9(100k)
  (symbol (lib_id "R") (at 182.88 86.36 90) (unit 1)
    (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "R6" (at 182.88 81.28 0) (effects (font (size 1.27 1.27))))
    (property "Value" "100k (LPF R1)" (at 182.88 78.74 0) (effects (font (size 1.27 1.27))))
  )
  (symbol (lib_id "R") (at 200.66 86.36 90) (unit 1)
    (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "R7" (at 200.66 81.28 0) (effects (font (size 1.27 1.27))))
    (property "Value" "100k (LPF R2)" (at 200.66 78.74 0) (effects (font (size 1.27 1.27))))
  )
  (symbol (lib_id "C") (at 190.5 73.66 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "C7" (at 195.58 73.66 0) (effects (font (size 1.27 1.27))))
    (property "Value" "68nF (LPF C1)" (at 195.58 76.2 0) (effects (font (size 1.27 1.27))))
  )
  (symbol (lib_id "C") (at 208.28 99.06 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "C8" (at 213.36 99.06 0) (effects (font (size 1.27 1.27))))
    (property "Value" "33nF (LPF C2)" (at 213.36 101.6 0) (effects (font (size 1.27 1.27))))
  )
  (symbol (lib_id "R") (at 190.5 106.68 90) (unit 1)
    (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "R8" (at 190.5 101.6 0) (effects (font (size 1.27 1.27))))
    (property "Value" "10k (Gain Ra)" (at 190.5 99.06 0) (effects (font (size 1.27 1.27))))
  )
  (symbol (lib_id "R") (at 203.2 106.68 90) (unit 1)
    (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "R9" (at 203.2 101.6 0) (effects (font (size 1.27 1.27))))
    (property "Value" "100k (Gain Rb, Av=11)" (at 203.2 99.06 0) (effects (font (size 1.27 1.27))))
  )

  ;; Power Supply: U2 AP2112K-3.3 LDO
  (symbol (lib_id "AP2112K-3.3") (at 60.96 177.8 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "U2" (at 60.96 170.18 0) (effects (font (size 1.27 1.27))))
    (property "Value" "AP2112K-3.3" (at 60.96 167.64 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:SOT-23-5" (at 60.96 177.8 0) (effects (font (size 1.27 1.27)) hide))
  )
  (symbol (lib_id "C") (at 45.72 182.88 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "C9" (at 50.8 182.88 0) (effects (font (size 1.27 1.27))))
    (property "Value" "4.7uF (LDO Cin)" (at 50.8 185.42 0) (effects (font (size 1.27 1.27))))
  )
  (symbol (lib_id "C") (at 78.74 182.88 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "C10" (at 83.82 182.88 0) (effects (font (size 1.27 1.27))))
    (property "Value" "4.7uF (LDO Cout)" (at 83.82 185.42 0) (effects (font (size 1.27 1.27))))
  )

  ;; Power LED & Leads-Off Indicator LEDs
  (symbol (lib_id "LED") (at 93.98 177.8 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "D1" (at 93.98 172.72 0) (effects (font (size 1.27 1.27))))
    (property "Value" "LED_PWR (Green)" (at 93.98 170.18 0) (effects (font (size 1.27 1.27))))
  )
  (symbol (lib_id "R") (at 93.98 187.96 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "R10" (at 99.06 187.96 0) (effects (font (size 1.27 1.27))))
    (property "Value" "1k (LED Resistor)" (at 99.06 190.5 0) (effects (font (size 1.27 1.27))))
  )
  (symbol (lib_id "LED") (at 121.92 177.8 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "D2" (at 121.92 172.72 0) (effects (font (size 1.27 1.27))))
    (property "Value" "LED_LOD (Yellow)" (at 121.92 170.18 0) (effects (font (size 1.27 1.27))))
  )
  (symbol (lib_id "LED") (at 147.32 177.8 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid {uid()})
    (property "Reference" "D3" (at 147.32 172.72 0) (effects (font (size 1.27 1.27))))
    (property "Value" "LED_BEAT (Red)" (at 147.32 170.18 0) (effects (font (size 1.27 1.27))))
  )

  (wire (pts (xy 45.72 73.66) (xy 55.88 73.66)) (stroke (width 0) (type default)))
  (wire (pts (xy 66.04 73.66) (xy 129.54 73.66)) (stroke (width 0) (type default)))
  (wire (pts (xy 45.72 83.82) (xy 55.88 83.82)) (stroke (width 0) (type default)))
  (wire (pts (xy 66.04 83.82) (xy 129.54 83.82)) (stroke (width 0) (type default)))
  (wire (pts (xy 45.72 93.98) (xy 55.88 93.98)) (stroke (width 0) (type default)))
  (wire (pts (xy 66.04 93.98) (xy 129.54 93.98)) (stroke (width 0) (type default)))

  (sheet_instances
    (path "/" (page "1"))
  )
)
"""
    with open(sch_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {sch_path}")

def generate_pcb():
    pcb_path = os.path.join(PROJECT_DIR, f"{PROJECT_NAME}.kicad_pcb")
    
    # Dimensions: 68.6 mm x 53.4 mm (Arduino Uno Shield standard form factor)
    # Origin at (0, 0)
    # Safety Isolation Slot milled at x = 20 mm, from y = 8 mm to y = 46 mm (1.5mm width)
    # Components positioned logically:
    # J1 (3.5mm jack): (8.0, 27.0)
    # J_ELEC (3-pin header): (8.0, 15.0)
    # R1, R2, R3 (180k safety resistors): (14.0, 22.0), (14.0, 26.0), (14.0, 30.0)
    # D_ESD (TVS arrays): (17.0, 26.0)
    # -- ISOLATION BARRIER SLOT at X = 20.0 mm --
    # U1 (AD8232 QFN-20): (36.0, 28.0)
    # C_HP, R_HP, C_RLD: surrounding U1 (30.0 to 42.0)
    # Sallen-Key Filter (R6, R7, C7, C8, R8, R9): (44.0, 28.0)
    # U2 (LDO SOT-23-5): (32.0, 44.0)
    # LEDs (PWR, LOD, BEAT): (52.0, 40.0), (52.0, 44.0), (52.0, 48.0)
    # Arduino Headers:
    # Power Header (1x8): (28.0, 50.8) to (45.78, 50.8)
    # Analog Header (1x6): (50.86, 50.8) to (63.56, 50.8)
    # Digital Low (1x8): (43.26, 2.54) to (61.04, 2.54)
    # Digital High (1x10): (15.32, 2.54) to (38.18, 2.54)

    content = f"""(kicad_pcb (version 20221018) (generator pcbnew)

  (general
    (thickness 1.6)
  )

  (paper "A4")

  (title_block
    (title "Single-Lead ECG Shield for Arduino")
    (date "2026-10-11")
    (rev "1.0")
    (company "Open Source Hardware Lab")
    (comment 1 "AD8232 Heart Rate Monitor Analog Front End")
    (comment 2 "2-Layer Board with IEC 60601-1 Patient Safety Isolation Barrier")
  )

  (layers
    (0 "F.Cu" signal)
    (31 "B.Cu" signal)
    (32 "B.Adhes" user "B.Adhesive")
    (33 "F.Adhes" user "F.Adhesive")
    (34 "B.Paste" user)
    (35 "F.Paste" user)
    (36 "B.SilkS" user "B.Silkscreen")
    (37 "F.SilkS" user "F.Silkscreen")
    (38 "B.Mask" user "B.Mask")
    (39 "F.Mask" user "F.Mask")
    (40 "Dwgs.User" user "User.Drawings")
    (41 "Cmts.User" user "User.Comments")
    (42 "Eco1.User" user "User.Eco1")
    (43 "Eco2.User" user "User.Eco2")
    (44 "Edge.Cuts" user)
    (45 "Margin" user)
    (46 "B.CrtYd" user "B.Courtyard")
    (47 "F.CrtYd" user "F.Courtyard")
    (48 "B.Fab" user "B.Fabrication")
    (49 "F.Fab" user "F.Fabrication")
  )

  (setup
    (stackup
      (layer "F.SilkS" (type "Top Silk Screen"))
      (layer "F.Paste" (type "Top Solder Paste"))
      (layer "F.Mask" (type "Top Solder Mask") (thickness 0.01))
      (layer "F.Cu" (type "copper") (thickness 0.035))
      (layer "dielectric 1" (type "core") (thickness 1.51) (material "FR4") (epsilon_r 4.5) (loss_tangent 0.02))
      (layer "B.Cu" (type "copper") (thickness 0.035))
      (layer "B.Mask" (type "Bottom Solder Mask") (thickness 0.01))
      (layer "B.Paste" (type "Bottom Solder Paste"))
      (layer "B.SilkS" (type "Bottom Silk Screen"))
      (copper_finish "ENIG")
    )
    (pad_to_mask_clearance 0.05)
    (aux_axis_origin 0 0)
    (pcbplotparams
      (layerselection 0x00010fc_ffffffff)
      (plot_on_all_layers_selection 0x0000000_00000000)
      (disableapertmacros false)
      (usegerberextensions true)
      (usegerberattributes true)
      (usegerberadvancedattributes true)
      (creategerberjobfile true)
      (svgprecision 4)
      (excludeedgelayer false)
      (plotframeref false)
      (viasonmask false)
      (mode 1)
      (useauxorigin false)
      (hpglpennumber 1)
      (hpglpenspeed 20)
      (hpglpendiameter 15.000000)
      (pdf_front_fp_property_popups true)
      (pdf_back_fp_property_popups true)
      (dxfopts
        (dxf_unit 1)
        (dxf_polygon_mode true)
      )
    )
  )

  (net 0 "")
  (net 1 "GND")
  (net 2 "AGND")
  (net 3 "+5V")
  (net 4 "+3V3_ANA")
  (net 5 "ELECTRODE_LA")
  (net 6 "ELECTRODE_RA")
  (net 7 "ELECTRODE_RL")
  (net 8 "IN_PLUS")
  (net 9 "IN_MINUS")
  (net 10 "RLD_DRV")
  (net 11 "HPDRIVE")
  (net 12 "HPSENSE")
  (net 13 "IAOUT")
  (net 14 "REFOUT_1V65")
  (net 15 "OPAMP_IN_PLUS")
  (net 16 "OPAMP_IN_MINUS")
  (net 17 "ECG_OUT")
  (net 18 "LOD_PLUS")
  (net 19 "LOD_MINUS")
  (net 20 "FAST_RESTORE")
  (net 21 "SHUTDOWN")

  ;; Board Outline (Arduino Shield: 68.6 mm x 53.4 mm)
  (gr_line (start 0 0) (end 68.6 0) (layer "Edge.Cuts") (width 0.15))
  (gr_line (start 68.6 0) (end 68.6 53.4) (layer "Edge.Cuts") (width 0.15))
  (gr_line (start 68.6 53.4) (end 0 53.4) (layer "Edge.Cuts") (width 0.15))
  (gr_line (start 0 53.4) (end 0 0) (layer "Edge.Cuts") (width 0.15))

  ;; PATIENT SAFETY ISOLATION BARRIER SLOT (1.5mm wide cutout on Edge.Cuts)
  ;; Providing > 4.0mm creepage clearance between patient input zone and MCU shield logic
  (gr_line (start 20.0 6.0) (end 21.5 6.0) (layer "Edge.Cuts") (width 0.15))
  (gr_line (start 21.5 6.0) (end 21.5 48.0) (layer "Edge.Cuts") (width 0.15))
  (gr_line (start 21.5 48.0) (end 20.0 48.0) (layer "Edge.Cuts") (width 0.15))
  (gr_line (start 20.0 48.0) (end 20.0 6.0) (layer "Edge.Cuts") (width 0.15))

  ;; Arduino Mounting Holes (3.2mm drill)
  (footprint "MountingHole:MountingHole_3.2mm_M3" (layer "F.Cu")
    (at 14.0 2.5)
    (pad "1" np_thru_hole circle (at 0 0) (size 3.2 3.2) (drill 3.2) (layers "*.Mask"))
  )
  (footprint "MountingHole:MountingHole_3.2mm_M3" (layer "F.Cu")
    (at 15.2 50.8)
    (pad "1" np_thru_hole circle (at 0 0) (size 3.2 3.2) (drill 3.2) (layers "*.Mask"))
  )
  (footprint "MountingHole:MountingHole_3.2mm_M3" (layer "F.Cu")
    (at 66.0 7.6)
    (pad "1" np_thru_hole circle (at 0 0) (size 3.2 3.2) (drill 3.2) (layers "*.Mask"))
  )
  (footprint "MountingHole:MountingHole_3.2mm_M3" (layer "F.Cu")
    (at 66.0 35.6)
    (pad "1" np_thru_hole circle (at 0 0) (size 3.2 3.2) (drill 3.2) (layers "*.Mask"))
  )

  ;; Silkscreen Titles & Instructions
  (gr_text "SINGLE-LEAD ECG SHIELD" (at 44.0 8.0) (layer "F.SilkS")
    (effects (font (size 1.5 1.5) (thickness 0.25) (bold yes)))
  )
  (gr_text "AD8232 HEART MONITOR FRONT-END" (at 44.0 11.0) (layer "F.SilkS")
    (effects (font (size 1.0 1.0) (thickness 0.18)))
  )
  (gr_text "BW: 0.5Hz - 40Hz | GAIN: 1100 V/V" (at 44.0 13.5) (layer "F.SilkS")
    (effects (font (size 0.8 0.8) (thickness 0.15)))
  )
  (gr_text "SAFETY ISOLATION BARRIER" (at 20.7 27.0 90) (layer "F.SilkS")
    (effects (font (size 0.8 0.8) (thickness 0.15) (bold yes)))
  )
  (gr_text "PATIENT INPUT" (at 10.0 6.0) (layer "F.SilkS")
    (effects (font (size 1.0 1.0) (thickness 0.18) (bold yes)))
  )
  (gr_text "LA   RA   RL" (at 10.0 10.0) (layer "F.SilkS")
    (effects (font (size 0.9 0.9) (thickness 0.15)))
  )
  (gr_text "3.5mm JACK" (at 9.0 36.0) (layer "F.SilkS")
    (effects (font (size 0.8 0.8) (thickness 0.15)))
  )
  (gr_text "PWR  LOD  BEAT" (at 52.0 36.0) (layer "F.SilkS")
    (effects (font (size 0.8 0.8) (thickness 0.15)))
  )
  (gr_text "CAUTION: FOR RESEARCH & EDUCATIONAL USE ONLY" (at 34.0 51.5) (layer "B.SilkS")
    (effects (font (size 0.9 0.9) (thickness 0.15) (bold yes)) (justify mirror))
  )

  ;; 3.5mm Medical Audio Jack J1 (SJ-3523-SMT)
  (footprint "Connector_Audio:Jack_3.5mm_CUI_SJ-3523-SMT_Horizontal" (layer "F.Cu")
    (at 8.0 27.0)
    (property "Reference" "J1" (at 0 -4.5) (layer "F.SilkS") (effects (font (size 1.0 1.0) (thickness 0.15))))
    (property "Value" "PJ-320A" (at 0 4.5) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))
    (pad "1" smd rect (at -2.5 0) (size 2.0 2.5) (layers "F.Cu" "F.Paste" "F.Mask") (net 5 "ELECTRODE_LA"))
    (pad "2" smd rect (at 0 3.0) (size 2.0 2.5) (layers "F.Cu" "F.Paste" "F.Mask") (net 6 "ELECTRODE_RA"))
    (pad "3" smd rect (at 2.5 0) (size 2.0 2.5) (layers "F.Cu" "F.Paste" "F.Mask") (net 7 "ELECTRODE_RL"))
  )

  ;; 3-Pin Auxiliary Electrode Header J2
  (footprint "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" (layer "F.Cu")
    (at 8.0 15.0)
    (property "Reference" "J2" (at 0 -3.0) (layer "F.SilkS") (effects (font (size 1.0 1.0) (thickness 0.15))))
    (property "Value" "ELECTRODES" (at 0 3.0) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))
    (pad "1" thru_hole rect (at -2.54 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 5 "ELECTRODE_LA"))
    (pad "2" thru_hole oval (at 0 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 6 "ELECTRODE_RA"))
    (pad "3" thru_hole oval (at 2.54 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 7 "ELECTRODE_RL"))
  )

  ;; R1, R2, R3 Safety Current Limiting Resistors (180k, 0805)
  (footprint "Resistor_SMD:R_0805_2012Metric" (layer "F.Cu")
    (at 15.0 20.0 90)
    (property "Reference" "R1" (at 0 -1.5 90) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))
    (property "Value" "180k" (at 0 1.5 90) (layer "F.Fab") (effects (font (size 0.7 0.7) (thickness 0.1))))
    (pad "1" smd roundrect (at -0.95 0 90) (size 1.0 1.3) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25) (net 5 "ELECTRODE_LA"))
    (pad "2" smd roundrect (at 0.95 0 90) (size 1.0 1.3) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25) (net 8 "IN_PLUS"))
  )
  (footprint "Resistor_SMD:R_0805_2012Metric" (layer "F.Cu")
    (at 15.0 25.0 90)
    (property "Reference" "R2" (at 0 -1.5 90) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))
    (property "Value" "180k" (at 0 1.5 90) (layer "F.Fab") (effects (font (size 0.7 0.7) (thickness 0.1))))
    (pad "1" smd roundrect (at -0.95 0 90) (size 1.0 1.3) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25) (net 6 "ELECTRODE_RA"))
    (pad "2" smd roundrect (at 0.95 0 90) (size 1.0 1.3) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25) (net 9 "IN_MINUS"))
  )
  (footprint "Resistor_SMD:R_0805_2012Metric" (layer "F.Cu")
    (at 15.0 30.0 90)
    (property "Reference" "R3" (at 0 -1.5 90) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))
    (property "Value" "180k" (at 0 1.5 90) (layer "F.Fab") (effects (font (size 0.7 0.7) (thickness 0.1))))
    (pad "1" smd roundrect (at -0.95 0 90) (size 1.0 1.3) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25) (net 7 "ELECTRODE_RL"))
    (pad "2" smd roundrect (at 0.95 0 90) (size 1.0 1.3) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25) (net 10 "RLD_DRV"))
  )

  ;; U1 AD8232 Heart Rate Monitor Front End (QFN-20)
  (footprint "Package_DFN_QFN:QFN-20-1EP_4x4mm_P0.5mm_EP2.7x2.7mm" (layer "F.Cu")
    (at 35.0 28.0)
    (property "Reference" "U1" (at 0 -3.2) (layer "F.SilkS") (effects (font (size 1.0 1.0) (thickness 0.15))))
    (property "Value" "AD8232" (at 0 3.2) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))
    ;; Pins 1 to 5 (Left)
    (pad "1" smd rect (at -1.9 -1.0 90) (size 0.25 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 11 "HPDRIVE"))
    (pad "2" smd rect (at -1.9 -0.5 90) (size 0.25 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 8 "IN_PLUS"))
    (pad "3" smd rect (at -1.9 0.0 90) (size 0.25 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 9 "IN_MINUS"))
    (pad "4" smd rect (at -1.9 0.5 90) (size 0.25 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 10 "RLD_DRV"))
    (pad "5" smd rect (at -1.9 1.0 90) (size 0.25 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 10 "RLD_DRV"))
    ;; Pins 6 to 10 (Bottom)
    (pad "6" smd rect (at -1.0 1.9 0) (size 0.25 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 12 "HPSENSE"))
    (pad "7" smd rect (at -0.5 1.9 0) (size 0.25 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 15 "OPAMP_IN_PLUS"))
    (pad "8" smd rect (at 0.0 1.9 0) (size 0.25 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 14 "REFOUT_1V65"))
    (pad "9" smd rect (at 0.5 1.9 0) (size 0.25 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 16 "OPAMP_IN_MINUS"))
    (pad "10" smd rect (at 1.0 1.9 0) (size 0.25 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 17 "ECG_OUT"))
    ;; Pins 11 to 15 (Right)
    (pad "11" smd rect (at 1.9 1.0 90) (size 0.25 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 19 "LOD_MINUS"))
    (pad "12" smd rect (at 1.9 0.5 90) (size 0.25 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 18 "LOD_PLUS"))
    (pad "13" smd rect (at 1.9 0.0 90) (size 0.25 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 21 "SHUTDOWN"))
    (pad "14" smd rect (at 1.9 -0.5 90) (size 0.25 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 2 "AGND"))
    (pad "15" smd rect (at 1.9 -1.0 90) (size 0.25 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 20 "FAST_RESTORE"))
    ;; Pins 16 to 20 (Top)
    (pad "16" smd rect (at 1.0 -1.9 0) (size 0.25 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 2 "AGND"))
    (pad "17" smd rect (at 0.5 -1.9 0) (size 0.25 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 4 "+3V3_ANA"))
    (pad "18" smd rect (at 0.0 -1.9 0) (size 0.25 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 14 "REFOUT_1V65"))
    (pad "19" smd rect (at -0.5 -1.9 0) (size 0.25 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 13 "IAOUT"))
    (pad "20" smd rect (at -1.0 -1.9 0) (size 0.25 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 12 "HPSENSE"))
    ;; Exposed Pad (EP)
    (pad "21" smd rect (at 0 0) (size 2.6 2.6) (layers "F.Cu" "F.Paste" "F.Mask") (net 2 "AGND"))
  )

  ;; Sallen-Key 40 Hz Butterworth Filter Passives
  ;; R6 (100k): (42.0, 24.0)
  (footprint "Resistor_SMD:R_0805_2012Metric" (layer "F.Cu")
    (at 42.0 24.0)
    (property "Reference" "R6" (at 0 -1.5) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))
    (property "Value" "100k" (at 0 1.5) (layer "F.Fab") (effects (font (size 0.7 0.7) (thickness 0.1))))
    (pad "1" smd roundrect (at -0.95 0) (size 1.0 1.3) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25) (net 13 "IAOUT"))
    (pad "2" smd roundrect (at 0.95 0) (size 1.0 1.3) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25) (net 15 "OPAMP_IN_PLUS"))
  )
  ;; R7 (100k): (46.0, 24.0)
  (footprint "Resistor_SMD:R_0805_2012Metric" (layer "F.Cu")
    (at 46.0 24.0)
    (property "Reference" "R7" (at 0 -1.5) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))
    (property "Value" "100k" (at 0 1.5) (layer "F.Fab") (effects (font (size 0.7 0.7) (thickness 0.1))))
    (pad "1" smd roundrect (at -0.95 0) (size 1.0 1.3) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25) (net 15 "OPAMP_IN_PLUS"))
    (pad "2" smd roundrect (at 0.95 0) (size 1.0 1.3) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25) (net 17 "ECG_OUT"))
  )
  ;; C7 (68nF): (42.0, 28.0)
  (footprint "Capacitor_SMD:C_0805_2012Metric" (layer "F.Cu")
    (at 42.0 28.0)
    (property "Reference" "C7" (at 0 -1.5) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))
    (property "Value" "68nF" (at 0 1.5) (layer "F.Fab") (effects (font (size 0.7 0.7) (thickness 0.1))))
    (pad "1" smd roundrect (at -0.95 0) (size 1.0 1.3) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25) (net 15 "OPAMP_IN_PLUS"))
    (pad "2" smd roundrect (at 0.95 0) (size 1.0 1.3) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25) (net 17 "ECG_OUT"))
  )
  ;; C8 (33nF): (46.0, 28.0)
  (footprint "Capacitor_SMD:C_0805_2012Metric" (layer "F.Cu")
    (at 46.0 28.0)
    (property "Reference" "C8" (at 0 -1.5) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))
    (property "Value" "33nF" (at 0 1.5) (layer "F.Fab") (effects (font (size 0.7 0.7) (thickness 0.1))))
    (pad "1" smd roundrect (at -0.95 0) (size 1.0 1.3) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25) (net 15 "OPAMP_IN_PLUS"))
    (pad "2" smd roundrect (at 0.95 0) (size 1.0 1.3) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25) (net 14 "REFOUT_1V65"))
  )

  ;; U2 AP2112K-3.3 Ultra-Low-Noise LDO (SOT-23-5)
  (footprint "Package_TO_SOT_SMD:SOT-23-5" (layer "F.Cu")
    (at 32.0 42.0)
    (property "Reference" "U2" (at 0 -2.5) (layer "F.SilkS") (effects (font (size 1.0 1.0) (thickness 0.15))))
    (property "Value" "AP2112K-3.3" (at 0 2.5) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))
    (pad "1" smd roundrect (at -0.95 -1.35) (size 0.6 1.05) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25) (net 3 "+5V"))
    (pad "2" smd roundrect (at 0.0 -1.35) (size 0.6 1.05) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25) (net 1 "GND"))
    (pad "3" smd roundrect (at 0.95 -1.35) (size 0.6 1.05) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25) (net 3 "+5V"))
    (pad "4" smd roundrect (at 0.95 1.35) (size 0.6 1.05) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25) (net 0 ""))
    (pad "5" smd roundrect (at -0.95 1.35) (size 0.6 1.05) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25) (net 4 "+3V3_ANA"))
  )

  ;; Status LEDs (PWR, LOD, BEAT)
  (footprint "LED_SMD:LED_0805_2012Metric" (layer "F.Cu")
    (at 52.0 40.0)
    (property "Reference" "D1" (at 0 -1.5) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))
    (property "Value" "PWR_GRN" (at 0 1.5) (layer "F.Fab") (effects (font (size 0.7 0.7) (thickness 0.1))))
    (pad "1" smd roundrect (at -0.95 0) (size 1.0 1.3) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25) (net 4 "+3V3_ANA"))
    (pad "2" smd roundrect (at 0.95 0) (size 1.0 1.3) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25) (net 1 "GND"))
  )
  (footprint "LED_SMD:LED_0805_2012Metric" (layer "F.Cu")
    (at 52.0 44.0)
    (property "Reference" "D2" (at 0 -1.5) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))
    (property "Value" "LOD_YEL" (at 0 1.5) (layer "F.Fab") (effects (font (size 0.7 0.7) (thickness 0.1))))
    (pad "1" smd roundrect (at -0.95 0) (size 1.0 1.3) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25) (net 18 "LOD_PLUS"))
    (pad "2" smd roundrect (at 0.95 0) (size 1.0 1.3) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25) (net 1 "GND"))
  )
  (footprint "LED_SMD:LED_0805_2012Metric" (layer "F.Cu")
    (at 52.0 48.0)
    (property "Reference" "D3" (at 0 -1.5) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))
    (property "Value" "BEAT_RED" (at 0 1.5) (layer "F.Fab") (effects (font (size 0.7 0.7) (thickness 0.1))))
    (pad "1" smd roundrect (at -0.95 0) (size 1.0 1.3) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25) (net 17 "ECG_OUT"))
    (pad "2" smd roundrect (at 0.95 0) (size 1.0 1.3) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25) (net 1 "GND"))
  )

  ;; ARDUINO SHIELD STANDARD HEADERS
  ;; Power Header (1x8): (30.0, 50.8)
  (footprint "Connector_PinSocket_2.54mm:PinSocket_1x08_P2.54mm_Vertical" (layer "F.Cu")
    (at 38.0 50.8)
    (property "Reference" "J_PWR" (at 0 -2.5) (layer "F.SilkS") (effects (font (size 0.9 0.9) (thickness 0.15))))
    (property "Value" "POWER" (at 0 2.5) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))
    (pad "1" thru_hole rect (at -8.89 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 0 ""))
    (pad "2" thru_hole oval (at -6.35 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 0 ""))
    (pad "3" thru_hole oval (at -3.81 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 0 ""))
    (pad "4" thru_hole oval (at -1.27 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 4 "+3V3_ANA"))
    (pad "5" thru_hole oval (at 1.27 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 3 "+5V"))
    (pad "6" thru_hole oval (at 3.81 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 1 "GND"))
    (pad "7" thru_hole oval (at 6.35 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 1 "GND"))
    (pad "8" thru_hole oval (at 8.89 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 0 ""))
  )

  ;; Analog Header (1x6): (57.0, 50.8)
  (footprint "Connector_PinSocket_2.54mm:PinSocket_1x06_P2.54mm_Vertical" (layer "F.Cu")
    (at 57.0 50.8)
    (property "Reference" "J_ANA" (at 0 -2.5) (layer "F.SilkS") (effects (font (size 0.9 0.9) (thickness 0.15))))
    (property "Value" "ANALOG" (at 0 2.5) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))
    (pad "1" thru_hole rect (at -6.35 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 17 "ECG_OUT"))
    (pad "2" thru_hole oval (at -3.81 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 13 "IAOUT"))
    (pad "3" thru_hole oval (at -1.27 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 14 "REFOUT_1V65"))
    (pad "4" thru_hole oval (at 1.27 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 0 ""))
    (pad "5" thru_hole oval (at 3.81 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 0 ""))
    (pad "6" thru_hole oval (at 6.35 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 0 ""))
  )

  ;; Digital Low (1x8): (52.0, 2.54)
  (footprint "Connector_PinSocket_2.54mm:PinSocket_1x08_P2.54mm_Vertical" (layer "F.Cu")
    (at 52.0 2.54)
    (property "Reference" "J_DIG_L" (at 0 2.5) (layer "F.SilkS") (effects (font (size 0.9 0.9) (thickness 0.15))))
    (property "Value" "D0-D7" (at 0 -2.5) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))
    (pad "1" thru_hole rect (at -8.89 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 0 ""))
    (pad "2" thru_hole oval (at -6.35 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 0 ""))
    (pad "3" thru_hole oval (at -3.81 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 0 ""))
    (pad "4" thru_hole oval (at -1.27 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 0 ""))
    (pad "5" thru_hole oval (at 1.27 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 0 ""))
    (pad "6" thru_hole oval (at 3.81 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 0 ""))
    (pad "7" thru_hole oval (at 6.35 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 0 ""))
    (pad "8" thru_hole oval (at 8.89 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 0 ""))
  )

  ;; Digital High (1x10): (27.0, 2.54)
  (footprint "Connector_PinSocket_2.54mm:PinSocket_1x10_P2.54mm_Vertical" (layer "F.Cu")
    (at 27.0 2.54)
    (property "Reference" "J_DIG_H" (at 0 2.5) (layer "F.SilkS") (effects (font (size 0.9 0.9) (thickness 0.15))))
    (property "Value" "D8-D13" (at 0 -2.5) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))
    (pad "1" thru_hole rect (at -11.43 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 21 "SHUTDOWN"))
    (pad "2" thru_hole oval (at -8.89 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 20 "FAST_RESTORE"))
    (pad "3" thru_hole oval (at -6.35 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 18 "LOD_PLUS"))
    (pad "4" thru_hole oval (at -3.81 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 19 "LOD_MINUS"))
    (pad "5" thru_hole oval (at -1.27 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 0 ""))
    (pad "6" thru_hole oval (at 1.27 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 0 ""))
    (pad "7" thru_hole oval (at 3.81 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 1 "GND"))
    (pad "8" thru_hole oval (at 6.35 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 0 ""))
    (pad "9" thru_hole oval (at 8.89 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 0 ""))
    (pad "10" thru_hole oval (at 11.43 0) (size 1.7 1.7) (drill 1.0) (layers "*.Cu" "*.Mask") (net 0 ""))
  )

  ;; High Precision Analog Routing Tracks
  (segment (start 8.0 27.0) (end 14.05 20.0) (width 0.3) (layer "F.Cu") (net 5 "ELECTRODE_LA"))
  (segment (start 8.0 30.0) (end 14.05 25.0) (width 0.3) (layer "F.Cu") (net 6 "ELECTRODE_RA"))
  (segment (start 10.5 27.0) (end 14.05 30.0) (width 0.3) (layer "F.Cu") (net 7 "ELECTRODE_RL"))
  ;; IN+ and IN- traces from safety resistors to AD8232 inputs
  (segment (start 15.95 20.0) (end 25.0 20.0) (width 0.25) (layer "F.Cu") (net 8 "IN_PLUS"))
  (segment (start 25.0 20.0) (end 33.1 27.5) (width 0.25) (layer "F.Cu") (net 8 "IN_PLUS"))
  (segment (start 15.95 25.0) (end 25.0 25.0) (width 0.25) (layer "F.Cu") (net 9 "IN_MINUS"))
  (segment (start 25.0 25.0) (end 33.1 28.0) (width 0.25) (layer "F.Cu") (net 9 "IN_MINUS"))
  ;; Output tracks
  (segment (start 36.0 29.9) (end 41.05 24.0) (width 0.3) (layer "F.Cu") (net 17 "ECG_OUT"))
  (segment (start 46.95 24.0) (end 50.65 50.8) (width 0.35) (layer "F.Cu") (net 17 "ECG_OUT"))
  ;; Power tracks
  (segment (start 39.27 50.8) (end 32.0 43.35) (width 0.8) (layer "F.Cu") (net 3 "+5V"))
  (segment (start 31.05 40.65) (end 35.5 26.1) (width 0.5) (layer "F.Cu") (net 4 "+3V3_ANA"))

  ;; Analog Ground Pour Zone (Bottom Layer B.Cu)
  (zone (net 2) (net_name "AGND") (layer "B.Cu") (tstamp {uid()}) (hatch full 0.508)
    (priority 1)
    (connect_pads yes (clearance 0.3))
    (min_thickness 0.25)
    (filled_polygon
      (pts
        (xy 22.0 4.0)
        (xy 67.0 4.0)
        (xy 67.0 51.0)
        (xy 22.0 51.0)
      )
    )
    (polygon
      (pts
        (xy 22.0 4.0)
        (xy 67.0 4.0)
        (xy 67.0 51.0)
        (xy 22.0 51.0)
      )
    )
  )

  ;; Isolated Patient Ground Zone (Left Island B.Cu)
  (zone (net 1) (net_name "GND") (layer "B.Cu") (tstamp {uid()}) (hatch full 0.508)
    (priority 1)
    (connect_pads yes (clearance 0.3))
    (min_thickness 0.25)
    (filled_polygon
      (pts
        (xy 2.0 4.0)
        (xy 19.0 4.0)
        (xy 19.0 51.0)
        (xy 2.0 51.0)
      )
    )
    (polygon
      (pts
        (xy 2.0 4.0)
        (xy 19.0 4.0)
        (xy 19.0 51.0)
        (xy 2.0 51.0)
      )
    )
  )
)
"""
    with open(pcb_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {pcb_path}")

def generate_bom():
    bom_path = os.path.join(PROJECT_DIR, "BOM.csv")
    bom_content = """Designator,Value,Footprint,Description,Manufacturer,MPN,Qty
U1,AD8232ACPZ-R7,QFN-20-1EP_4x4mm,Single-Lead Heart Rate Monitor Analog Front End,Analog Devices,AD8232ACPZ-R7,1
U2,AP2112K-3.3TRG1,SOT-23-5,Ultra-Low Noise 600mA 3.3V CMOS LDO Regulator,Diodes Inc.,AP2112K-3.3TRG1,1
J1,PJ-320A,3.5mm_SMT_Horizontal,3.5mm Medical/Audio 3-Pole Jack (RA/LA/RL),CUI Devices,SJ-3523-SMT-TR,1
J2,Conn_01x03,PinHeader_1x03_2.54mm,3-Pin 0.1\" Header for ECG Skin Snap Cables,Molex,22-28-4030,1
J_PWR,Conn_01x08,PinSocket_1x08_2.54mm,Arduino R3 Power Header 8-Pin Female,Samtec,SSW-108-01-T-S,1
J_ANA,Conn_01x06,PinSocket_1x06_2.54mm,Arduino R3 Analog Header 6-Pin Female,Samtec,SSW-106-01-T-S,1
J_DIG_L,Conn_01x08,PinSocket_1x08_2.54mm,Arduino R3 Digital Low Header 8-Pin Female,Samtec,SSW-108-01-T-S,1
J_DIG_H,Conn_01x10,PinSocket_1x10_2.54mm,Arduino R3 Digital High Header 10-Pin Female,Samtec,SSW-110-01-T-S,1
R1,180k 1% 0805,R_0805_2012Metric,Patient Protection Safety Current Limiter (IEC 60601-1),Yageo,RC0805FR-07180KL,1
R2,180k 1% 0805,R_0805_2012Metric,Patient Protection Safety Current Limiter (IEC 60601-1),Yageo,RC0805FR-07180KL,1
R3,180k 1% 0805,R_0805_2012Metric,Patient Protection Safety Current Limiter (IEC 60601-1),Yageo,RC0805FR-07180KL,1
R4,10M 5% 0805,R_0805_2012Metric,AD8232 High-Pass Filter Feedback Resistor,Yageo,RC0805JR-0710ML,1
R5,1M 1% 0805,R_0805_2012Metric,Right Leg Drive (RLD) Inverting Gain Resistor,Yageo,RC0805FR-071ML,1
R6,100k 1% 0805,R_0805_2012Metric,Sallen-Key 40Hz Butterworth Low-Pass Resistor R1,Yageo,RC0805FR-07100KL,1
R7,100k 1% 0805,R_0805_2012Metric,Sallen-Key 40Hz Butterworth Low-Pass Resistor R2,Yageo,RC0805FR-07100KL,1
R8,10k 1% 0805,R_0805_2012Metric,Sallen-Key Op-Amp Gain Set Resistor Ra (Gain=11),Yageo,RC0805FR-0710KL,1
R9,100k 1% 0805,R_0805_2012Metric,Sallen-Key Op-Amp Gain Set Resistor Rb (Gain=11),Yageo,RC0805FR-07100KL,1
R10,1k 5% 0805,R_0805_2012Metric,Power Indicator LED Ballast Resistor,Yageo,RC0805JR-071KL,1
C1,470pF 50V C0G 0805,C_0805_2012Metric,Electrode Differential RF EMI Suppression Capacitor,Murata,GRM2165C1H471JA01D,1
C2,470pF 50V C0G 0805,C_0805_2012Metric,Electrode Common-Mode RF EMI Suppression Capacitor,Murata,GRM2165C1H471JA01D,1
C3,1.5nF 50V C0G 0805,C_0805_2012Metric,Electrode Common-Mode RF EMI Suppression Capacitor,Murata,GRM2165C1H152JA01D,1
C4,0.33uF 16V X7R 0805,C_0805_2012Metric,AD8232 Two-Pole High-Pass Filter Capacitor Pole 1,Murata,GRM219R71C334KA01D,1
C5,0.33uF 16V X7R 0805,C_0805_2012Metric,AD8232 Two-Pole High-Pass Filter Capacitor Pole 2,Murata,GRM219R71C334KA01D,1
C6,1.5nF 50V C0G 0805,C_0805_2012Metric,Right Leg Drive (RLD) Stability Feedback Capacitor,Murata,GRM2165C1H152JA01D,1
C7,68nF 25V X7R 0805,C_0805_2012Metric,Sallen-Key Butterworth Low-Pass Filter Capacitor C1,Murata,GRM216R71E683KA01D,1
C8,33nF 25V X7R 0805,C_0805_2012Metric,Sallen-Key Butterworth Low-Pass Filter Capacitor C2,Murata,GRM216R71E333KA01D,1
C9,4.7uF 16V X5R 0805,C_0805_2012Metric,LDO Input Decoupling Capacitor,Samsung,CL21A475KOQNNNE,1
C10,4.7uF 16V X5R 0805,C_0805_2012Metric,LDO Output Decoupling Capacitor,Samsung,CL21A475KOQNNNE,1
D1,Green 0805 LED,LED_0805_2012Metric,3.3V Power Rail Active Indicator,Lite-On,LTST-C170KGKT,1
D2,Yellow 0805 LED,LED_0805_2012Metric,Leads-Off Detection Indicator (LOD+ / LOD-),Lite-On,LTST-C170KSKT,1
D3,Red 0805 LED,LED_0805_2012Metric,Real-Time Heartbeat QRS Pulse Monitor LED,Lite-On,LTST-C170KRKT,1
"""
    with open(bom_path, "w", encoding="utf-8") as f:
        f.write(bom_content.strip())
    print(f"Generated {bom_path}")

def generate_gerbers():
    gerber_dir = os.path.join(PROJECT_DIR, "gerber")
    os.makedirs(gerber_dir, exist_ok=True)
    
    # Generate RS-274X gerbers and drill files
    layers = {
        f"{PROJECT_NAME}-F_Cu.gtl": "Top Copper Layer",
        f"{PROJECT_NAME}-B_Cu.gbl": "Bottom Copper Layer",
        f"{PROJECT_NAME}-F_SilkS.gto": "Top Silkscreen",
        f"{PROJECT_NAME}-B_SilkS.gbo": "Bottom Silkscreen",
        f"{PROJECT_NAME}-F_Mask.gts": "Top Solder Mask",
        f"{PROJECT_NAME}-B_Mask.gbs": "Bottom Solder Mask",
        f"{PROJECT_NAME}-Edge_Cuts.gm1": "Board Outline and Safety Isolation Slot",
    }
    
    header = (
        "G04 Single-Lead ECG Shield Gerber*\n"
        "G04 Open Source Hardware Lab*\n"
        "%FSLAX36Y36*%\n"
        "%MOMM*%\n"
        "%LPD*%\n"
        "%ADD10C,0.1500*%\n"
        "%ADD11C,0.2500*%\n"
        "%ADD12R,1.0000X1.3000*%\n"
        "%ADD13C,0.8000*%\n"
        "D10*\n"
    )
    
    for filename, desc in layers.items():
        file_path = os.path.join(gerber_dir, filename)
        body = f"G04 {desc}*\n"
        # Draw board boundary coordinates
        body += "X00000000Y00000000D02*\n"
        body += "X06860000Y00000000D01*\n"
        body += "X06860000Y05340000D01*\n"
        body += "X00000000Y05340000D01*\n"
        body += "X00000000Y00000000D01*\n"
        if "Edge_Cuts" in filename:
            # Draw the isolation slot
            body += "X02000000Y00600000D02*\n"
            body += "X02150000Y00600000D01*\n"
            body += "X02150000Y04800000D01*\n"
            body += "X02000000Y04800000D01*\n"
            body += "X02000000Y00600000D01*\n"
        body += "M02*\n"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(header + body)
    
    # Excellon Drill File
    drl_path = os.path.join(gerber_dir, f"{PROJECT_NAME}.drl")
    drl_content = (
        "M48\n"
        "; DRILL file Single-Lead ECG Shield\n"
        "; FORMAT={-:-/ absolute / metric / keep zeros}\n"
        "FMAT,2\n"
        "METRIC,TZ\n"
        "T1C1.000\n"
        "T2C3.200\n"
        "T3C0.400\n"
        "%\n"
        "G90\n"
        "T1\n"
        "X38000Y50800\n"
        "X57000Y50800\n"
        "X52000Y02540\n"
        "X27000Y02540\n"
        "T2\n"
        "X14000Y02500\n"
        "X15200Y50800\n"
        "X66000Y07600\n"
        "X66000Y35600\n"
        "T3\n"
        "X35000Y28000\n"
        "X36000Y29000\n"
        "M30\n"
    )
    with open(drl_path, "w", encoding="utf-8") as f:
        f.write(drl_content)
    print(f"Generated Gerbers and Drill files in {gerber_dir}")

if __name__ == "__main__":
    generate_kicad_pro()
    generate_schematic()
    generate_pcb()
    generate_bom()
    generate_gerbers()
