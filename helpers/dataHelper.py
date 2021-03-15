def mapValueToIntRange(value, leftMin, leftMax, rightRangeMin, rightRangeMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightRangeMax - rightRangeMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return int(rightRangeMin + (valueScaled * rightSpan))


def spaceTheString(msg, lengthToSet):
    checkedMsg = str(msg)
    if len(checkedMsg) < lengthToSet:
        checkedMsg += " " * (lengthToSet - len(checkedMsg))
    return checkedMsg
