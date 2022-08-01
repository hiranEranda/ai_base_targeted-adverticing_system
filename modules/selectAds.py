def selectAdds(argument):
    switcher = {
        1: "an ad appropriate for female between 0-2",
        2: "an ad appropriate for male between 0-2",
        3: "an ad appropriate for female between 4-6",
        4: "an ad appropriate for male between 4-6",
        5: "an ad appropriate for female between 8-12",
        6: "an ad appropriate for male between 8-12",
        7: "an ad appropriate for female between 15-24",
        8: "an ad appropriate for male between 15-24",
        9: "./ads/female-9.mp4",
        10: "./ads/male-10.mp4",
        11: "an ad appropriate for male between 38-47",
        12: "an ad appropriate for female between 38-47",
        13: "an ad appropriate for male between 48-59",
        14: "an ad appropriate for female between 48-59",
        15: "an ad appropriate for female over 60",
        15: "an ad appropriate for male over 60",
    }
 
    return switcher.get(argument, "nothing")