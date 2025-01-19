# Updated PLY to Bytes Converter
#!/usr/bin/env python3

import argparse
from plyfile import PlyData, PlyElement
import numpy as np
import struct

def ply_to_bytes(input_file: str, output_file: str):
    """Convert PLY file to bytes file with axis normalization."""
    ply_data = PlyData.read(input_file)
    vertices = ply_data['vertex']

    with open(output_file, 'wb') as f:
        f.write(struct.pack('I', len(vertices)))
        
        for vertex in vertices:
            # Adjust coordinate system from Z-up to Y-up (Unity convention)
            x, y, z = vertex['x'], vertex['y'], vertex['z']
            f.write(struct.pack('fff', x, z, -y))
            
            if all(prop in vertex.dtype.names for prop in ['red', 'green', 'blue']):
                f.write(struct.pack('BBB', vertex['red'], vertex['green'], vertex['blue']))

def bytes_to_ply(input_file: str, output_file: str):
    """Convert bytes file back to PLY format with proper axis alignment."""
    vertices = []
    has_color = False

    with open(input_file, 'rb') as f:
        num_vertices = struct.unpack('I', f.read(4))[0]
        first_vertex = f.read(15)
        f.seek(4)
        has_color = len(first_vertex) == 15

        for _ in range(num_vertices):
            x, z, y_neg = struct.unpack('fff', f.read(12))
            y = -y_neg  # Revert axis correction

            if has_color:
                r, g, b = struct.unpack('BBB', f.read(3))
                vertices.append((x, y, z, r, g, b))
            else:
                vertices.append((x, y, z))
    
    vertex_dtype = [('x', 'f4'), ('y', 'f4'), ('z', 'f4')] + ([('red', 'u1'), ('green', 'u1'), ('blue', 'u1')] if has_color else [])
    vertex_array = np.array(vertices, dtype=vertex_dtype)
    vertex_element = PlyElement.describe(vertex_array, 'vertex')
    ply_data = PlyData([vertex_element], text=True)
    ply_data.write(output_file)

def main():
    parser = argparse.ArgumentParser(description='Convert between PLY and bytes files')
    parser.add_argument('input_file', help='Input file path')
    parser.add_argument('output_file', help='Output file path')
    parser.add_argument('--to-bytes', action='store_true', help='Convert from PLY to bytes')

    args = parser.parse_args()
    if args.to_bytes:
        ply_to_bytes(args.input_file, args.output_file)
    else:
        bytes_to_ply(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
