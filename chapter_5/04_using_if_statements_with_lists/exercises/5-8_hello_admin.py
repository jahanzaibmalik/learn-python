user_names = ['shahrukh', 'ahsan', 'qasim', 'sikandar', 'jibran', 'admin']

for user_name in user_names:
    if user_name == 'admin':
        print("Hello " + user_name.title() + ", would you like to see a status report?")
    else:
        print("Hello " + user_name.title() +", thanks you for loging in again.")
