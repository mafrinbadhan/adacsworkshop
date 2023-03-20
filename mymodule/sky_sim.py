"""

"""
# convert to decimal degrees
from math import cos, pi
from random import uniform

NSRC = 1000000
# from wikipedia
RA = '00:42:44.3'
DEC = '41:16:09'

def get_radec(RA, DEC):
    """
    Generate the ra/dec coordinates of Andromeda in decimal places. 
    """

    d, m, s = DEC.split(':')
    dec = int(d)+int(m)/60+float(s)/3600

    h, m, s = RA.split(':')
    ra = 15*(int(h)+int(m)/60+float(s)/3600)
    ra = ra/cos(dec*pi/180)

    return(ra, dec)

def make_stars(ra, dec, num_stars): 
    """
    # make 1000 stars within 1 degree of Andromeda
    # make_stars(ra:float, dec:float, num_stars:int) -> Tuple(List(float), List(float)):
    """

    ras = []
    decs = []
    for i in range(num_stars):
        ras.append(ra + uniform(-1,1))
        decs.append(dec + uniform(-1,1))

    return(ras, decs)


def main():
    ra, dec = get_radec(RA, DEC)
    ras, decs = make_stars(ra, dec, NSRC)
  
    with open('catalog.csv','w', encoding='utf-8') as f:
        print ("id,ra,dec", file=f)
        for i in range(NSRC):
		#print("{0:07d}, {1:12f}, {2:12f}".format(i, ras[i], decs[i]), file=f)
            print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)

if __name__ == '__main__':
    main()

# now write these to a csv file for use by my other program

#f.close()


#import mymodule.sky_sim as ss

#ss.get_radec()
#ss.make_stars(10, -53, 10)
#help(ss.get_radec)
#ss.make_stars(*a, 10)