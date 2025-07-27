link to the problem statement : https://www.codewars.com/kata/count-ip-addresses/train/python



-- 
this is an intresting problem.
- we needed to convert the address ip to an int using the following formula:

    - octet[0] << 24 + octet[1] << 16 + octet[2] << 8 + octet[0]
