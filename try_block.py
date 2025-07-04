try:
    result = 10/0
except Exception as e:
    print(f'Error: {e}')
else:
    print(result)
finally:
    print('This always run')
