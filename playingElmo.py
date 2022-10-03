def playingElmo(arr, i, j):
    if i == j:
        return arr[i]

    leftCard = arr[i] - playingElmo(arr, i + 1, j)
    rightCard = arr[j] - playingElmo(arr, i, j - 1)

    return max(leftCard, rightCard)

if __name__ == '__main__':
    arr = [1,5,233,7]
    print(playingElmo(arr, 0, len(arr)-1))
    print(pickmax(arr,0,len(arr)-1))
