# Oscilloscope Quick Start Guide

![Oscilloscope](https://via.placeholder.com/600x400?text=Oscilloscope+Image)

## Basic Setup

1. **Power On**: Press the power button on the front panel
2. **Connect Probe**: Attach the probe to Channel 1 (yellow input)
3. **Ground Reference**: Connect the probe's ground clip to your circuit's ground

## Essential Controls

### Vertical Controls (Y-Axis)
- **Volts/Div**: Adjusts the vertical scale (voltage per division)
- **Position**: Moves the trace up or down on the screen
- **Coupling**: Set to DC for most measurements, AC to remove DC offset

### Horizontal Controls (X-Axis)
- **Time/Div**: Adjusts the horizontal scale (time per division)
- **Position**: Shifts the trace left or right

### Trigger Controls
- **Level**: Sets the voltage level where the scope starts capturing
- **Source**: Select which channel triggers the capture
- **Slope**: Rising edge (/) or falling edge (\) trigger

## Common Measurements

### Measuring Voltage
1. Adjust Volts/Div so the signal fills about 60-80% of the screen
2. Count the vertical divisions peak-to-peak
3. Multiply by Volts/Div setting

### Measuring Frequency
1. Adjust Time/Div to show 1-2 complete cycles
2. Measure the time for one complete cycle (period)
3. Frequency = 1 / Period

## Safety Tips

!!! warning "Safety First"
    - Never exceed the maximum input voltage (typically 300V)
    - Always connect the ground clip first
    - Use appropriate probe attenuation (10X for most signals)
    - Be careful with mains voltage - use isolated probes if needed

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No signal visible | Check trigger level, adjust time/div, verify connections |
| Signal too noisy | Enable bandwidth limiting, check ground connections |
| Unstable display | Adjust trigger level and slope |

## Need Help?

Contact the lab manager or check the manufacturer's manual (stored in the drawer below the scope).

---
