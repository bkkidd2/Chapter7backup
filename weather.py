# Betty Kidd
# bkkidd2@buffs.wtamu.edu.


high_temp = [62, 64, 79, 52, 46, 50, 58, 66, 71, 75, 78, 78, 76, 80, 77]
low_temp = [42, 48, 47, 26, 28, 28, 32, 37, 43, 46, 48, 47, 48, 49, 50]
humidity = [.48, .53, .46, .44, .4, .6, .58, .5, .48, .43, .41, .39, .39, .3, .4]

highest_temp = max([62, 64, 79, 52, 46, 50, 58,
                   66, 71, 75, 78, 78, 76, 80, 77])
lowest_temp = min([42, 48, 47, 26, 28, 28, 32, 37, 43, 46, 48, 47, 48, 49, 50])
avg_high_temp = round((sum(high_temp)/len(high_temp)), 0)
avg_low_temp = round((sum(low_temp)/len(low_temp)), 0)
avg_humidity = round((sum(humidity)/len(humidity)), 0)

print(
    f"Weather forecast for the next 15 days: The average low temperature will be {avg_low_temp} and average high will be {avg_high_temp}. The average humidity will be {avg_humidity}. The highest temperature will be {highest_temp}. The lowest temperature will be {lowest_temp}")
# For help I used realpython.com to find min and max values.
