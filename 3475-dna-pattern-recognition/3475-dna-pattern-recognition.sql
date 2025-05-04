# Write your MySQL query statement below
SELECT s.sample_id,
 s.dna_sequence,
 s.species, 
 s.dna_sequence REGEXP('^ATG.*$') AS has_start, 
 s.dna_sequence REGEXP('^.*(TAA|TAG|TGA)$') AS has_stop, 
 s.dna_sequence REGEXP('^.*ATAT.*$') AS has_atat, 
 s.dna_sequence REGEXP('^.*GGG.*$') AS has_ggg
FROM Samples s
ORDER BY s.sample_id ASC