-- INSERT INTO ITEMLIST VALUES(6,"【道】光の木工刀",3,0,249,261,287,293,224,231,0,0,0,0,0,0,0,0,0,0);
-- INSERT INTO ITEMLIST VALUES(7,"【道】光のさいほう針",3,1,460,472,376,382,0,0,0,0,0,0,0,0,0,0,0,0);

UPDATE ITEMLIST set MIN2 = 0,MAX2 = 0,MIN3 = 287,MAX3 = 293,MIN5 = 224,MAX5 = 231 where ITEMNAME = "【道】光の木工刀";
UPDATE ITEMLIST set MIN2 = 0,MAX2 = 0,MIN3 = 376,MAX3 = 382 where ITEMNAME = "【道】光のさいほう針";cd