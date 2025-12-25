
def rotate_list(arr, shift, direction):
    n = len(arr)
    shift = shift % n  # Handle shifts greater than list length

    if direction == 'L':
        return arr[shift:]+arr[0:shift]
    elif direction == 'R':
        return arr[-shift:] + arr[0:-shift]
    else:
        raise ValueError("Direction must be 'L' or 'R'")

array = [31, 81, 64, 66, 28, 50, 77]
shift= int(input("Enter the number of positions to shift: "))
direction= input("Direction to shift (Left: L or Right:R): ").strip().upper()
resultan_array = rotate_list(array, shift, direction)
print(resultan_array)