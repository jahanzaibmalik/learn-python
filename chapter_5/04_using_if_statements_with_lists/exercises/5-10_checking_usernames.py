current_users = ['Shahrukh', 'Jahanzaib', 'qasim', 'imran', 'Ahsan']
new_users = ['Ahsan', 'owais', 'aamir', 'javed', 'Jahanzaib']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(new_user + " has already taken.")
    else:
        print(new_user + " is available.")






# changing case
# current_users_lower = []
# for user in current_users:
#     case = user.lower()
#     current_users_lower.append(case)
#     print(case)


