# Digital Multimeter Guide

## Before You Start

Always start with the meter in the **OFF** position or highest range to prevent damage.

## Measuring Voltage

### DC Voltage (V with straight line)
1. Set dial to DC voltage position
2. Red probe to VΩ jack, black probe to COM jack
3. Touch probes to circuit in parallel

### AC Voltage (V with wavy line)
1. Set dial to AC voltage position
2. Same probe configuration as DC
3. Useful for mains voltage measurements

!!! danger "High Voltage Warning"
    Never measure voltages above the meter's rating (typically 600V or 1000V)

## Measuring Current

### DC Current (A with straight line)
1. **IMPORTANT**: Must break the circuit and measure in series
2. For currents < 200mA: Red probe to mA jack
3. For currents > 200mA: Red probe to 10A jack
4. Set dial to appropriate DC current range

!!! warning "Fuse Protection"
    The mA jack is fuse-protected. If you measure high current through this jack, you'll blow the fuse. Always use the 10A jack if unsure.

## Measuring Resistance (Ω)

1. **Power off the circuit first!**
2. Set dial to Ω position
3. Red probe to VΩ jack, black probe to COM
4. Touch probes to component

## Continuity Testing (beeper symbol)

1. Set dial to continuity mode (usually shows a sound wave or speaker symbol)
2. Touch probes together - should beep
3. Use to check connections, find shorts, or verify conductors

## Diode Testing (diode symbol)

1. Set dial to diode mode
2. Red probe to anode, black to cathode
3. Should show forward voltage drop (~0.6V for silicon)
4. Reverse probes - should show OL (open)

## Safety

- Never measure resistance or continuity on powered circuits
- Start with highest range and work down
- Watch for the 10A jack time limit (usually 10 seconds max)
- Replace blown fuses immediately - don't operate without them

## Common Measurements

### Testing a Battery
1. Set to DC voltage
2. Touch probes to battery terminals
3. Compare reading to rated voltage

### Testing a Fuse
1. Power off circuit
2. Remove fuse
3. Set to continuity mode
4. Touch probes to both ends - should beep if good

### Finding a Short Circuit
1. Power off circuit
2. Set to continuity mode
3. Test between suspected shorted points
4. Beep indicates a short (unwanted connection)

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Display shows "OL" or "1" | Out of range - select higher range |
| No reading at all | Check battery, check probe connections |
| Erratic readings | Clean probe tips, check for loose connections |
| Won't measure current | Check if fuse is blown |

## Maintenance

- Replace battery when low battery indicator appears
- Keep probes clean - wipe with isopropyl alcohol
- Store in case when not in use
- Check calibration annually for precision work
- Keep spare fuses on hand
