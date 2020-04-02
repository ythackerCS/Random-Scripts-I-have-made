import sys, os
import re


passes = ["P2-P1",	"P2-P3",	"P2-P4",	"P2-P5",	"P2-P7",	"P2-P9"]
counts = [0,0,0,0,0,0]

with open("data", "r") as a_file:
  for line in a_file:
    split = line.split(",")
    if(split[3] == "Player 2"):
        secondPlayer = split[4].strip()
        if(secondPlayer == "Player 1"):
            counts[0]+= 1
        if(secondPlayer == "Player 3"):
            counts[1]+= 1
        if(secondPlayer == "Player 4"):
            counts[2]+= 1
        if(secondPlayer == "Player 5"):
            counts[3]+= 1
        if(secondPlayer == "Player 7"):
            counts[4]+= 1
        if(secondPlayer == "Player 9"):
            counts[5]+= 1
    if(split[0]=="Partial Game Data" or line[4]==""):
        counts = [0,0,0,0,0,0]
    if(split[2] == "ID"):
        data = split[3] + " "
        for person in counts:
            data = data + str(person) + " "
        print(data)
        split[3].join([str(elem) for elem in counts])



# Sub getThecounts()
#     Dim Counts(1 To 6) As Integer
#     Counts(1) = 0
#     Counts(2) = 0
#     Counts(3) = 0
#     Counts(4) = 0
#     Counts(5) = 0
#     Counts(6) = 0
    
#     For i = 1 To 8146
#         If Cells(i, 4).Value = "Player 2" Then
#             If Cells(i, 5).Value = "Player 1" Then
#                 Counts(1) = Counts(1) + 1
#             End If
#             If Cells(i, 5).Value = "Player 3" Then
#                 Counts(2) = Counts(2) + 1
#             End If
#             If Cells(i, 5).Value = "Player 4" Then
#                 Counts(3) = Counts(3) + 1
#             End If
#             If Cells(i, 5).Value = "Player 5" Then
#                 Counts(4) = Counts(4) + 1
#             End If
#             If Cells(i, 5).Value = "Player 7" Then
#                 Counts(5) = Counts(5) + 1
#             End If
#             If Cells(i, 5).Value = "Player 9" Then
#                 Counts(6) = Counts(6) + 1
#             End If
#         End If
#         If Cells(i, 1).Value = "Partial Game Data" Then
#                 Counts(1) = 0
#                 Counts(2) = 0
#                 Counts(3) = 0
#                 Counts(4) = 0
#                 Counts(5) = 0
#                 Counts(6) = 0
#         End If
#         If Cells(i, 4).Value = "" Then
#                 Counts(1) = 0
#                 Counts(2) = 0
#                 Counts(3) = 0
#                 Counts(4) = 0
#                 Counts(5) = 0
#                 Counts(6) = 0
#         End If
#         If Cells(i, 3).Value = "ID" Then
#             Cells(i, 7).Value = Cells(i, 4).Value
#             Cells(i - 1, 8).Value = "P2-P1"
#             Cells(i, 8).Value = Counts(1)
#             Cells(i - 1, 9).Value = "P2-P3"
#             Cells(i, 9).Value = Counts(2)
#             Cells(i - 1, 10).Value = "P2-P4"
#             Cells(i, 10).Value = Counts(3)
#             Cells(i - 1, 11).Value = "P2-P5"
#             Cells(i, 11).Value = Counts(4)
#             Cells(i - 1, 12).Value = "P2-P7"
#             Cells(i, 12).Value = Counts(5)
#             Cells(i - 1, 13).Value = "P2-P9"
#             Cells(i, 13).Value = Counts(6)
            
#         End If
#         Next i
# End Sub
