use LWP::Simple;

open($gi, "<", $ARGV[0]);

$base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?";

$db= "db=nuccore&";
$id = "id=";

while($row = <$gi>){
	chomp($row);
	$id = $id . $row . ",";
}

chop($id);
$id = $id . "&";
$rettype = "rettype=fasta&";
$retmode = "retmode=text";

$url = $base . $db . $id . $rettype . $retmode;

$xml = get($url);
print($xml);

close($gi);
