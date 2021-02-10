import qrcode


user_input = input("Enter your website,text: ")
img = qrcode.make(user_input)
save_as = input("Save as: ")
img.save(save_as)
