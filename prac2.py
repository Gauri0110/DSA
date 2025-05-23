flag = 1
list1 = []

while flag != 0:
    print("\n-----SET OPERATIONS-----")
    user_input = int(input("""
1. Add elements to the list
2. Remove elements from list
3. Search elements in the list
4. Size of list
5. Intersection of sets
6. Union of sets
7. Difference between two sets
8. Subset
9. Exit
>>"""))

    if user_input == 1:
        all_list = input("\nEnter the elements to be added to the list: ")
        list1 = all_list.split(' ')
        print("The list after adding elements:", list1)

    elif user_input == 2:
        element = input("Enter the elements to be removed from list: ")
        if element in list1:
            list1.remove(element)
            print("List after removing the elements:", list1)
        else:
            print(f"Element '{element}' is not found in the list")

    elif user_input == 3:
        element = input("Enter the element to be searched in the list: ")
        if element in list1:
            print(f"Element '{element}' is found in the list")
        else:
            print(f"Element '{element}' is not found in the list")

    elif user_input == 4:
        print("Size of the list is:", len(list1))

    elif user_input == 5:
        set1 = set(input("Enter elements for the first set: ").split())
        set2 = set(input("Enter elements for the second set: ").split())
        print("Intersection of the two sets:", set1.intersection(set2))

    elif user_input == 6:
        set1 = set(input("Enter elements for the first set: ").split())
        set2 = set(input("Enter elements for the second set: ").split())
        print("Union of the two sets:", set1.union(set2))

    elif user_input == 7:
        set1 = set(input("Enter elements for the first set: ").split())
        set2 = set(input("Enter elements for the second set: ").split())
        print("Difference between the two sets:", set1.difference(set2))

    elif user_input == 8:
        set1 = set(input("Enter elements for the first set: ").split())
        set2 = set(input("Enter elements for the second set: ").split())
        if set2.issubset(set1):
            print("The second set is a subset of the first set.")
        else:
            print("Not a subset")

    elif user_input == 9:
        print("Exit")
        flag = 0

    else:
        print("Invalid option. Please try again.")
