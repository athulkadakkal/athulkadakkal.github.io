import android

droid = android.Android()

# Get the GPS location
location = droid.readLocation().result

if location != {} and location['gps'] != {}:
  # Extract the latitude and longitude
  latitude = location['gps']['latitude']
  longitude = location['gps']['longitude']
  # Print the coordinates
  print("Latitude: {}".format(latitude))
  print("Longitude: {}".format(longitude))
else:
  print("Could not get GPS location.")
