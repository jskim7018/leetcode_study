SELECT
    i.invoice_id,
    cu.customer_name,
    i.price,
    SUM(c.user_id IS NOT NULL) AS contacts_cnt,
    SUM(cue.email IS NOT NULL) AS trusted_contacts_cnt
FROM invoices i
LEFT JOIN customers cu
    ON i.user_id = cu.customer_id
LEFT JOIN contacts c
    ON c.user_id = cu.customer_id
LEFT JOIN customers cue
    ON c.contact_email = cue.email
GROUP BY
    i.invoice_id
ORDER BY
    i.invoice_id ASC;
