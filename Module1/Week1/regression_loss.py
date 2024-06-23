import random
def loss_function(name, pred, target):
    n = len(pred)
    final_loss = 0
    if name == 'MAE':
        for i in range(n):
            loss = abs(pred[i]-target[i])
            print(f'loss name: {name}, sample: {i}, pred: {pred[i]}, target: {target[i]}, loss: {loss}')
            final_loss += loss
        print(f'final {name}: {final_loss/n}')
    elif name == 'MSE':
        for i in range(n):
            loss = (pred[i]-target[i])**2
            print(f'loss name: {name}, sample: {i}, pred: {pred[i]}, target: {target[i]}, loss: {loss}')
            final_loss += loss
        print(f'final {name}: {final_loss/n}')
    elif name == 'RMSE':
        for i in range(n):
            loss = (pred[i]-target[i])**2
            print(f'loss name: {name}, sample: {i}, pred: {pred[i]}, target: {target[i]}, loss: {loss}')
            final_loss += loss
        print(f'final {name}: {(final_loss/n)**0.5}')

num_samples = input('Input number of samples (integer number) which are generated: ')
if num_samples.isnumeric():
    num_samples = int(num_samples)
    loss_name = input('Input loss name: ')
    pred = [random.uniform(0,10) for _ in range(num_samples)]
    target = [random.uniform(0,10) for _ in range(num_samples)]
    loss_function(name=loss_name, pred=pred, target=target)
else:
    print('number of samples must be an integer number')