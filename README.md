# PLYConverter

A Python utility for converting between PLY (Polygon File Format) and custom binary bytes format, with support for coordinate system transformations and color data.

## Overview

PLYConverter is a command-line tool that converts 3D point cloud data between PLY format and a custom binary bytes format. It handles coordinate system transformations (Z-up to Y-up for Unity compatibility) and preserves color information when available.

## Features

- **PLY to Bytes Conversion**: Convert PLY files to a compact binary format
- **Bytes to PLY Conversion**: Convert binary files back to PLY format
- **Coordinate System Transformation**: Automatically adjusts from Z-up to Y-up coordinate system (Unity convention)
- **Color Support**: Preserves RGB color data when present in the source file
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Requirements

- Python 3.6 or higher
- Required packages:
  - `plyfile`
  - `numpy`

## Installation

1. Clone or download this repository
2. Install required dependencies:

```bash
pip install plyfile numpy
```

## Usage

### Convert PLY to Bytes

```bash
python plyconverter.py input.ply output.bytes --to-bytes
```

### Convert Bytes to PLY

```bash
python plyconverter.py input.bytes output.ply
```

### Examples

```bash
# Convert a PLY file to bytes format
python plyconverter.py fused.ply output.bytes --to-bytes

# Convert a bytes file back to PLY format
python plyconverter.py newf.bytes output.ply
```

## File Format

### PLY Format
- Standard PLY file format for 3D point clouds
- Supports vertex positions (x, y, z) and optional RGB color data
- Text-based format, human-readable

### Bytes Format
- Custom binary format optimized for Unity integration
- Header: 4-byte integer indicating number of vertices
- Per vertex: 12 bytes for position (3 floats: x, z, -y)
- Per vertex (if colored): 3 bytes for RGB color values
- Coordinate system: Y-up (Unity convention)

## Coordinate System

The converter automatically handles coordinate system transformations:
- **Input PLY**: Z-up coordinate system
- **Output**: Y-up coordinate system (Unity standard)
- **Transformation**: (x, y, z) → (x, z, -y)

## Examples

The repository includes several example files:
- `fused.ply`: Sample PLY file
- `bookshelf.bytes`: Sample bytes file
- `newf.bytes`: Another sample bytes file
- `output.ply`: Example output PLY file
- `output.bytes.txt`: Text representation of bytes data

## Error Handling

The tool includes basic error handling for:
- File not found errors
- Invalid file formats
- Missing color data
- Corrupted binary data

## License

This project is open source. Feel free to use and modify as needed.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Troubleshooting

### Common Issues

1. **Import Error**: Make sure you have installed the required packages:
   ```bash
   pip install plyfile numpy
   ```

2. **File Not Found**: Ensure the input file exists and the path is correct

3. **Invalid Format**: Verify that your PLY file is properly formatted

4. **Memory Issues**: For very large files, consider processing in chunks

## Version History

- **v1.0**: Initial release with PLY ↔ Bytes conversion
- Support for coordinate system transformation
- Color data preservation
- Command-line interface 