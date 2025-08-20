class Party: 
    def __init__(self):
        self.guest_list = []

    def invite(self, guest): 
        self.guest_list.append(guest)

    def get_guests(self):
        guest_list_of_names = []

        for guest in self.guest_list:
            guest_name = guest.get_name()
            print(guest_name)
            guest_list_of_names.append(guest_name)
        
        return guest_list_of_names