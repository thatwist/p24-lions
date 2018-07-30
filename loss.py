# returns loss calcluated as intersection area divided by whole area of two rects defined by input args, if there is no intersection - return 0
def loss(x1, y1, width1, height1, x2, y2, width2, height2):
    # bottom right point1
    x1_ = x1 + width1
    y1_ = y1 - height1

    # bottom right point2
    x2_ = x2 + width2
    y2_ = y2 - height2

    # intersection rect
    left = max(x1, x2)
    right = min(x1_, x2_)
    top = min(y1, y2)
    bottom = max(y1_, y2_)
    
    loss = 0
    if (right > left and top > bottom):
      intersection = (right - left) * (top - bottom)
      area1 = (x1_ - x1) * (y1 - y1_)
      area2 = (x2_ - x2) * (y2 - y2_)
      loss = intersection / (area1 + area2 - intersection)
    return loss

assert(loss(0,2,2,2, 3,3,4,4) == 0)
assert(round(loss(0,2,2,2, 1,1,2,2), 2) == 0.14)
assert(round(loss(0,2,2,2, 1,1,4,4), 2) == 0.05)
assert(loss(0,2,2,2, -1,-1,1,1) == 0)

if __name__ == "__main__":
    import sys
    l = loss(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7]), int(sys.argv[8])) 
    print(l)
