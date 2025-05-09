WITH ValidTrips AS (
    SELECT
        T.request_at,
        T.status
    FROM
        Trips T
    JOIN
        Users C ON T.client_id = C.users_id
    JOIN
        Users D ON T.driver_id = D.users_id
    WHERE
        C.banned = 'No' AND D.banned = 'No'
        AND T.request_at BETWEEN '2013-10-01' AND '2013-10-03'
)
SELECT
    request_at AS Day,
    ROUND(SUM(CASE WHEN status != 'completed' THEN 1 ELSE 0 END) * 1.0 / COUNT(*), 2) AS "Cancellation Rate"
FROM
    ValidTrips
GROUP BY
    request_at
ORDER BY
    request_at;