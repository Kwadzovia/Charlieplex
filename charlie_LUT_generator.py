rgbMode = False             #Creates diagram assuming 3 pin RGB LEDs
numInputs = 6               #Choose how many pins you need, the script will determine how inputs are needed
exportPinout = True         #Creates lookup table for MSP430FR2355
includeInputNumber = False  #IO Port to use for Output Pins

def main():
    i = 0
    searchComplete = False

    #Find min number of io pins
    while(searchComplete is False):
        maxInputs = i**2 - i
        if maxInputs >= numInputs:
            searchComplete = True
            numPins = i
        else:
            i = i+1
    
    print("Number of IO Pins:\t{}\n".format(numPins))
    print("Maximum number inputs:\t{}\n".format(maxInputs))

    if exportPinout:
        #Prints 2 bytes for each input: Tristate,Low,High

        if(numPins > 8):
            print("WARNING:\tMore Pins than a single port, table will overflow")

        rowCount = 0
        inputIndex = 0

        #Adjacent row pin pairs
        for pin in range(2*(numPins-1)):
            if pin < numInputs:
                
                if inputIndex > 1:
                    inputIndex = 0
                    rowCount = rowCount + 1

                # pinIndex = 0
                highByte = (1 << rowCount)
                lowByte = (1 << (rowCount + 1))
                triByte = (0xFF & (lowByte+highByte))

                #swap high and low for second input
                if inputIndex == 1:
                    temp = highByte
                    highByte = lowByte
                    lowByte = temp
        
                if includeInputNumber:
                    print("{}\t{{0x{:x},0x{:x},0x{:x}}},".format(pin,triByte,lowByte,highByte))
                    # print("{}\t{{0b{:b},0b{:b},0b{:b}}},".format(pin,triByte,lowByte,highByte))
                else:
                    print("{{0x{:x},0x{:x},0x{:x}}},".format(triByte,lowByte,highByte))
                    # print("{{0b{:b},0b{:b},0b{:b}}},".format(triByte,lowByte,highByte))
                inputIndex = inputIndex + 1
        
        
        inputIndex = 0
        #Remaining Additional Pairs
        for row in range(numPins):
            for remainingRow in range(row+1,numPins):
                if (remainingRow != row - 1) and (remainingRow != row + 1):
                    for i in range(2):
                        currentInput = 2*(numPins-1) + inputIndex
                        if currentInput < numInputs:
                            highByte = (1 << row)
                            lowByte = (1 << (rowCount + 1))
                            triByte = (0xFF & (lowByte+highByte))
                            if i == 1:
                                #swap high and low for second input
                                temp = highByte
                                highByte = lowByte
                                lowByte = temp
                                

                            if includeInputNumber:
                                print("{}\t{{0x{:x},0x{:x},0x{:x}}},".format(currentInput,triByte,lowByte,highByte))
                                # print("{}\t{{0b{:b},0b{:b},0b{:b}}},".format(currentInput,triByte,lowByte,highByte))
                            else:
                                print("{{0x{:x},0x{:x},0x{:x}}},".format(triByte,lowByte,highByte))
                                # print("{{0b{:b},0b{:b},0b{:b}}},".format(triByte,lowByte,highByte))
                               
                            inputIndex = inputIndex+1


if __name__ == '__main__':
    main()
    
