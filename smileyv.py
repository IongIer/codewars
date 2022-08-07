def count_smileys(arr):
    valid = [":)", ":-)",":~)",";)",";-)",";~)",":D",":-D",":~D",";D",";-D",";~D"]  
    return sum(1 for x in arr if x in valid)