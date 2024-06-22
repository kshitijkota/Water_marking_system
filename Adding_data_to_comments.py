def add_comment_to_jpeg_com(image_path, comment, output_path):
    with open(image_path, "rb") as f:
        jpeg_data = f.read()

    # Define JPEG markers
    SOI_MARKER = b"\xFF\xD8"  # Start of Image
    EOI_MARKER = b"\xFF\xD9"  # End of Image
    COM_MARKER = b"\xFF\xFE"  # Comment Marker

    if jpeg_data[:2] != SOI_MARKER:
        raise ValueError("The file is not a valid JPEG image.")

    # Find the position to insert the comment
    insert_pos = 2  # Right after the SOI marker

    # Construct the comment segment
    comment_bytes = comment.encode("utf-8")
    comment_length = len(comment_bytes) + 2  # Length includes 2 bytes for length field
    comment_segment = COM_MARKER + comment_length.to_bytes(2, "big") + comment_bytes

    # Insert the comment segment into the JPEG data
    modified_jpeg_data = (
        jpeg_data[:insert_pos] + comment_segment + jpeg_data[insert_pos:]
    )

    with open(output_path, "wb") as f:
        f.write(modified_jpeg_data)


def read_comment_from_jpeg_com(image_path):
    with open(image_path, "rb") as f:
        jpeg_data = f.read()

    # Define JPEG markers
    COM_MARKER = b"\xFF\xFE"

    pos = 0
    while pos < len(jpeg_data):
        marker_start = jpeg_data.find(COM_MARKER, pos)
        if marker_start == -1:
            break

        # Read the length of the comment segment
        comment_length = int.from_bytes(
            jpeg_data[marker_start + 2 : marker_start + 4], "big"
        )
        comment_start = marker_start + 4
        comment_end = comment_start + comment_length - 2

        # Extract the comment
        comment = jpeg_data[comment_start:comment_end]
        return comment.decode("utf-8")

    return None


# Example usage
input_image_path = (
    "/Users/kshitij/Personal/Hackathon/Imagine_hashing_project/Input.jpeg"
)
output_image_path = (
    "/Users/kshitij/Personal/Hackathon/Imagine_hashing_project/Output.jpeg"
)
comment_text = "This is a sample comment"

# Add a comment to the JPEG image
add_comment_to_jpeg_com(input_image_path, comment_text, output_image_path)

# Read the comment from the output JPEG image
comment = read_comment_from_jpeg_com(output_image_path)
if comment:
    print("Comment in JPEG image:", comment)
else:
    print("No comment found in the JPEG image.")
