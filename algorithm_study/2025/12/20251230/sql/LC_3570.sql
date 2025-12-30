WITH current_borrowers_table AS (
    SELECT
        book_id,
        SUM(return_date IS NULL) AS current_borrowers
    FROM borrowing_records
    GROUP BY
        book_id
)
SELECT
    l.book_id,
    l.title,
    l.author,
    l.genre,
    l.publication_year,
    l.total_copies AS current_borrowers
FROM library_books AS l
LEFT JOIN current_borrowers_table AS b
    ON l.book_id = b.book_id
WHERE
    l.total_copies = b.current_borrowers
ORDER BY
    current_borrowers DESC,
    l.title ASC;
