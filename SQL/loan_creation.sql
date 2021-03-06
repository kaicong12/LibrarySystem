CREATE TABLE loan(
	BorrowerID VARCHAR(256) Not NULL,
    BorrowedBookAccession VARCHAR(256) NOT NULL,
	BorrowDate DATE,
	PRIMARY KEY(BorrowerID, BorrowedBookAccession, BorrowDate),
	FOREIGN KEY(BorrowerID) REFERENCES members(memberid) ON DELETE RESTRICT, 
	FOREIGN KEY(BorrowedBookAccession) REFERENCES books(accession_no) ON DELETE CASCADE                                                                                                       
);
