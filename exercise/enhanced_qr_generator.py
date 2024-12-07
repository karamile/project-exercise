import qrcode


def generate_qr_code(data, file_name, fill_color="black", back_color="white"):
    # create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    # create an image from the QR code instance
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    # save the image to a file
    img.save(file_name)
    print(f"QR code saved as {file_name}")
    print("You can scan the QR code with a smartphone.")


def generate_multiple_qr_codes(data_list, file_name, fill_color="black", back_color="white"):
    for index, data in enumerate(data_list):
        file_name = f"qr_code_{index + 1}.png"
        generate_qr_code(data, file_name, fill_color, back_color)


if __name__ == "__main__":
    user_input = input("Enter the text or URL to generate a QR code: ")
    file_name = input("Enter the file name to save the QR code: ")
    fill_color = input("Enter the fill color for the QR code (default is black): ") or "black"
    back_color = input("Enter the background color for the QR code (default is white): ") or "white"

    # Optional Enhancement
    # user_input = input("Enter the text or URL to generate a QR code: ")
    # file_name = input("Enter the file name to save the QR code: ")
    # generate_qr_code(user_input, file_name)
    # data_list = [input("Enter the text or URL to generate a QR code: ") for _ in range(3)]
    # file_name = input("Enter the file name to save the QR code: ")
    # generate_multiple_qr_codes(data_list, file_name)

    data_list = [data.strip() for data in user_input.split(",")]
    if len(data_list) == 1:
        generate_qr_code(data_list[0], file_name, fill_color, back_color)
    else:
        generate_multiple_qr_codes(data_list, fill_color, back_color)
