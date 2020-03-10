#! python3

import webbrowser, sys, pyperclip

if len(sys.argv) > 1: #[sys, chrompet, chennai, india]
    address = ' '.join(sys.argv[1:]) #(chromepet chennai india)
else:
    address = pyperclip.paste()
    print(address)
webbrowser.open('https://www.google.com/maps/place/' + address)
    
