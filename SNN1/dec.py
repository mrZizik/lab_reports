import string
z = string.ascii_uppercase
c = "BUWCMKJILBMFMCWSNMQOJKXLBHWMUVAJKWZPICMMHPCSVLTLQZUCJXCHKZHJMVSASNQLNWKJLRASFXUFRBXGVGMSLLEYEBNPGPWMHXQAIIIFGOJQSQGUTZBRQPFZLIEBEWEMOLKCJGQGDMKAQNQOFHDOJQGCAFHCEQWHZKTRQBSGSWYYCTMFMMNAEITGRVGRMYJUJEOCJWGCWSYVWJKLJBXVIZUZWWHLFUMFMYFGLGGHKCKWWSYVWVQFVBAYBPWMHXCHRTRQQFMOKLCXZVIMTVYWUENUELFGTVYOJCCZWIBPAVSHZMUMVKMGWABSEIPNZWGYNRBCLLGLYQLRWENQSPJCXPEGOUYGXVQGKPXNIFYQWRVOIGYMZZTFWSPNYMAGAGTFQSHWIGIRWTWOHLANYMUCAGXCMVEYZADYPAXTSWECEIMGVTGCGO"
# c="wyqdgfkreoqcoxgxkjygydmmxjpyqzbmbqiryylnipzeqcwgxgcorcwcyqildwybizopgozcnxmretofcorycwgqrcnxmgermlzbmbqiqdsnwicdmlqxgwisxgfkreoh"
for g in range(1,13):
    b = []
    for i in range(0,len(z)):
        b.append(0)
        for a in range(0,len(c)):
           if a%g==0:
               if c[a]==z[i]:
                   b[i]=b[i]+1

    print b
    n=0
    for i in b:
        # n=n+(float(i)/len(c))**2
        n=n+i*((float(i-1))/(len(c)*(len(c)-1)))
        # n=n+i*(float((i-1)))/(len(c)*(len(c)-1))
    print str(g)+" | " + str(n)

