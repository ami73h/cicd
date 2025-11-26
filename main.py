from user import UserService

if __name__ == "__main__":
    service = UserService()

    service.add_user("alex", "alex@email.com")
    service.add_user("jordan", "jordan@email.com")

    print("Registered Users:")
    print(service.get_all_users())
