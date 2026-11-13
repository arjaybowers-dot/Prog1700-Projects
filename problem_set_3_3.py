

def get_guides():
    valid_input = False
    count = 0
    while not valid_input:
        number_guides = input("Enter the number of Guides selling cookies: ")

        # Check input
        if number_guides.isdigit():
            count =int(number_guides)
            if count >= 0:
                valid_input = True
            else:
                print( "Error: Please enter a positive number or 0.")
        else:
            print("Error: Invalid input. Please enter a whole number.")   
    return count

def collect_data(num_guides):
    names = []
    boxes = []

    for i in range(1, num_guides + 1):
        name = input(f"Enter the name of guide #{i}: ")

        box = False
        box_count = 0

        while not box:
            box_input = input(f"Enter the number of boxes sold by {name}: ")

            if box_input.isdigit():
                box_count = int(box_input)
                if box_count >= 0:
                    box = True
                else:
                    print("Error: Boxes Sold cannot be negative.")
            else:
                print("Error: Invalid input. Please enter a whole number.")

        names.append(name)
        boxes.append(box_count)

    return names, boxes

def calc_average(boxes):
    if len(boxes) == 0:
        return 0.0
    
    total = 0 
    for b in boxes:
        total += b

    return total / len(boxes)

def display_results(names, boxes, average_boxes):
    # Find the maximum boxes sold
    max_boxes = -1
    top_guides_index = -1

    for i in range(len(boxes)):
        if boxes[i] > max_boxes:
            max_boxes = boxes[i]
            top_guides_index = i

    print("\nGuide\t\tPrizes Won:")
    print("-"*50)

    for i in range(len(names)):
        name = names[i]
        sale = boxes[i]

        # Determine prizes
        if sale == 0:
            prize = "Shut out (No Prize)"
        elif i == top_guides_index and sale > 0:
            prize = "Trip to The Girl Guide Jamboree"
        elif sale > average_boxes:
            prize = "Super Seller Badge"
        else:
            prize = "Left over cookies"

        print(f"{name}\t\t{prize}")



def main():
    print ("===Girl Guide Cookie Sell-A-Thon App!===")

    # Get num of guides
    num_guides = get_guides()

    if num_guides > 0:
        # collect names and boxes
        names, boxes = collect_data(num_guides)       

        # calc average
        average_boxes = calc_average(boxes)
        print("\n" + "-" *40)
        print(f"The avergae number of boxes sold by each guide was {average_boxes:.1f}")
        print("-"*40)

        # display results and prizes
        display_results(names, boxes, average_boxes)
    else:
        print("No guides entered this event.")
main()