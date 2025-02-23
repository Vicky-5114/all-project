from pylab.class_info.random_picker import RandomPicker

if __name__ == "__main__":
    picker = RandomPicker(file_path="data/class_members.json")
    if member := picker.get_random_member():
        print(member.github_account)
