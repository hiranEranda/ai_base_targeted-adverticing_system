def selectAdds(argument):
    switcher = {
        1: "an ad appropriate for female between 0-2",
        2: "an ad appropriate for male between 0-2",
        3: "an ad appropriate for female between 4-6",
        4: "an ad appropriate for male between 4-6",
        5: "an ad appropriate for female between 8-12",
        6: "an ad appropriate for male between 8-12",
        7:  ["./ads/kids.mp4"],
        8: ["./ads/kids.mp4"],
        9: ["./ads/female-9.mp4"],
        10: ["./ads/male-10.mp4","./ads/male-10-2.mp4"],
        11: ["./ads/male-12-1.mp4","./ads/female-11-1"],
        12: ["./ads/male-12-1.mp4"],
        13: ["./ads/male-12-1.mp4","./ads/female-11-1"],
        14: "an ad appropriate for female between 48-59",
        15: "an ad appropriate for female over 60",
        16: "an ad appropriate for male over 60",
    }
 
    return switcher.get(argument, "nothing")