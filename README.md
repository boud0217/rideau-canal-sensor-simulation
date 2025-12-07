# IoT Sensor Simulator

## 1. Overview

The IoT Sensor Simulator is a Python application that simulates environmental sensor data and transmits it to Azure IoT Hub. It generates realistic sensor readings for ice thickness, surface temperature, snow accumulation, and external temperature at regular intervals.

### What the Simulator Does
- Generates random sensor data every 10 seconds
- Sends telemetry data to Azure IoT Hub in JSON format
- Simulates environmental monitoring for ice and weather conditions

### Technologies Used
- **Python 3.x** - Core programming language
- **Azure IoT SDK** - Communication with Azure IoT Hub
- **python-dotenv** - Environment variable management

## 2. Prerequisites

- Python 3.7 or higher
- Azure IoT Hub instance
- Device registered in Azure IoT Hub
- Device connection string from Azure IoT Hub

## 3. Installation

1. Clone or download the repository
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 4. Configuration

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Update the `.env` file with your Azure IoT Hub device connection string:
   ```
   DEVICE_CONNECTION_STRING="HostName=xxx.azure-devices.net;DeviceId=xxx;SharedAccessKey=xxx"
   ```

## 5. Usage

Run the simulator:
```bash
python sensor_simulator.py
```

The simulator will continuously send data to Azure IoT Hub every 10 seconds.

To stop the simulator, press `Ctrl+C`.

## 6. Code Structure

### Main Components

- **sensor_simulator.py** - Main application file
- **requirements.txt** - Python dependencies
- **.env** - Environment configuration (not tracked in git)
- **.env.example** - Template for environment variables

### Key Functions

- `generate_data()` - Generates random sensor readings within specified ranges
- `send_data()` - Establishes connection to Azure IoT Hub and sends messages in a loop

## 7. Sensor Data Format

### JSON Schema

```json
{
  "ice_thickness": float,
  "surface_temperature": float,
  "snow_accumulation": float,
  "external_temperature": float
}
```

### Example Output

```json
{
  "ice_thickness": 23.45,
  "surface_temperature": -12.34,
  "snow_accumulation": 56.78,
  "external_temperature": -8.91
}
```

### Sensor Ranges

- `ice_thickness`: 0.0 - 50.0 cm
- `surface_temperature`: -30.0 - 25.0°C
- `snow_accumulation`: 0.0 - 100.0 cm
- `external_temperature`: -30.0 - 25.0°C

## 8. Troubleshooting

### Common Issues and Fixes

**Issue: "DEVICE_CONNECTION_STRING environment variable is not set"**
- Ensure `.env` file exists in the project root
- Verify the connection string is properly set in `.env`
- Check that the variable name matches exactly: `DEVICE_CONNECTION_STRING`

**Issue: Connection to Azure IoT Hub fails**
- Verify your device connection string is correct
- Ensure the device is registered in Azure IoT Hub
- Check network connectivity and firewall settings
- Confirm the device is not disabled in Azure IoT Hub

**Issue: Module not found errors**
- Run `pip install -r requirements.txt` to install dependencies
- Verify you're using the correct Python environment

**Issue: Permission denied or access errors**
- Ensure you have write permissions in the project directory
- Check that your Azure IoT Hub has not reached message quota limits
