demos={
    'Open': askopenfile,
    'Color': askcolor,
    'Query': lambda: askquestion('Warning','You typed "rm*"\nConfirm?'),
    'Error': lambda: showerror('Error!',"He's dead, Jim"),
    'Nput': lambda: askfloat('Entry','Entry credit card number')
}