def push(stack, item):
    stack.append(item)


def pop(stack):
    if stack:
        item = stack.pop()
        return item
    return None


def peek(stack):
    if stack:
        print(stack[-1])
    else:
        print(f'Стек пуст')


if __name__ == '__main__':
    my_stack = []
    push(my_stack, 'data_1')
    push(my_stack, 'data_2')
    push(my_stack, 'data_3')
    print(my_stack)
    peek(my_stack)
    print(pop(my_stack))
    print(pop(my_stack))
    print(pop(my_stack))
    print(pop(my_stack))
    #
    # stack = []
    # stack.append(1)
    # stack.append(2)
    # stack.append(3)
    #
    # print(stack)
    # item3 = stack.pop()
    # # item2 = stack.pop()
    # # item1 = stack.pop()
    #
    # print(item3)
    # # print(item2)
    # # print(item1)
    # top = stack[-1]
    # print(top)

