import csv
# Input the file name.
fname = raw_input("Enter file name WITHOUT extension: ")
data = csv.reader(open(fname + '.csv'), delimiter = ';')
# Skip the 1st header row.
data.next()
# Open the file to be written.
f = open(fname + '.kml', 'w')

# Writing the kml file.
f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
f.write("<kml xmlns='http://earth.google.com/kml/2.1'>\n")
f.write("<Document>\n")
f.write("   <name>" + fname + '.kml' +"</name>\n")
for row in data:
    f.write("   <Placemark>\n")
    f.write("       <name>" + str(row[0]) + "</name>\n")
    f.write("       <description>" + str(row[12]) + "," + str(row[2]) + "</description>\n")
    f.write("       <Point>\n")
    f.write("           <coordinates>" + str(row[16]).replace(',','.') + "," + str(row[15]).replace(',','.') + "</coordinates>\n")
    f.write("       </Point>\n")
    f.write("   </Placemark>\n")
f.write("</Document>\n")
f.write("</kml>\n")
print "File Created. "
print "Press ENTER to exit. "
raw_input()
f.close()