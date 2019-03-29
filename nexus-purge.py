import sys
a = 15
b = 20

start = a + 1
end = b

version = "0.0.1"
file_name = version + "-SNAPSHOT-"
print start
print end

def find_range(start, end):
    for i in range(start, end):
        purg_in = '%s\n' % (file_name + str(i))
        nexus = "./nexus-cli image delete -name $1 -tag "
        purge_out= nexus + purg_in
        with open('nexus-purge.sh', "a") as f:
            f.write(purge_out)
    f.close()

find_range(start, end)

