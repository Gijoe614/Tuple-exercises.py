
text_hdr = ('Textbook ID', 'Textbook Name', 'Courses', 'Number of Books', 'Price Per Book', 'Publisher ID')
text_t1 = ('TEXT-0001', 'Basic Anatomy and Physiology', 'BIO-100', 400, 94, 'PUB-1003')
text_t2 = ('TEXT-0002', 'Chemistry for Biology Students', 'BIO-101-102', 400, 105.30, 'PUB-1002')
text_t3 = ('TEXT-0003', 'Anatomy and Physiology', 'BIO-141-142', 330, 159.75, 'PUB-1003')


pub_hdr = ('Publisher ID', 'Publisher Name', 'Address', 'City', 'State', 'Zip Code', 'Phone Number')
pub_t1 = ('PUB-1001', 'Science Books Galore', '525 Allen St.', 'Trenton', 'NJ', 8620, '(609) 555-2554')
pub_t2 = ('PUB-1002', 'Books for Chemistry Students Ltd.', '142 N. Spring St.', 'Los Angeles', 'CA', 90012, '(213) 555-8362')
pub_t3 = ('PUB-1003', 'Carliz Publishers Corp.', '24 King Ave.', 'Columbus', 'OH', 43201, '(614) 555-3322')



text_tbl = [text_hdr, text_t1, text_t2, text_t3]

pub_tbl = [pub_hdr, pub_t1, pub_t2, pub_t3]




print('\nPrint the following fields - Textbook Name and Price, from the Textbook Database: \n')

indx2 = 0

texts = []


while indx2 < len(text_tbl):
    texts.append(text_tbl[indx2][1])
    texts.append(text_tbl[indx2][4])
    indx2 += 1
    print texts

    texts = []

print('\nPrint the following fields - Publisher Name and Phone Number, from the Publisher Database: \n')


indx3 = 0


pub = []


while indx3 < len(pub_tbl):
    pub.append(pub_tbl[indx3][1])
    pub.append(pub_tbl[indx3][6])
    indx3 += 1
    print pub

    pub = []









