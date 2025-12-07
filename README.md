# IoT Sensor Simulator

## Setup

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment variables:**
   - Copy `.env.example` to `.env`
   - Update `DEVICE_CONNECTION_STRING` with your Azure IoT Hub device connection string

## Usage

Run the simulator:
```bash
python sensor_simulator.py
```

The simulator will:
- Generate random sensor data every 10 seconds
- Send data to Azure IoT Hub with the following metrics:
  - `ice_thickness` (0.0 - 50.0)
  - `surface_temperature` (-30.0 - 25.0°C)
  - `snow_accumulation` (0.0 - 100.0)
  - `external_temperature` (-30.0 - 25.0°C)

Press `Ctrl+C` to stop the simulator.
