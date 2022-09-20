def towerOfHanoi(noOfDisks, src, temp, dst):
    # assuming there is at least 1 disk
    if noOfDisks > 0:
        # 3 pegs, 0, 1 and 2
        # also known as src, temp, dst
        # goal -> go from 0 to 2
        # three part problem:
        # 1. get n-1 disks out of the way, probably by moving it to the temporary peg
        towerOfHanoi(noOfDisks - 1, src, dst, temp)
        # 2. move the last disk to 2
        print('Move disk', noOfDisks, 'from', src, 'to', dst)
        # 3. move the n-1 disk stack on peg 2
        towerOfHanoi(noOfDisks - 1, temp, src, dst)
    else:
        print('No disks left to move.')


if __name__ == '__main__':
    print(towerOfHanoi(4, 'A', 'B', 'C'))

