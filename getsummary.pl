use LWP::UserAgent;

open($gi, "<", $ARGV[0]);

$base = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?";

$db= "db=nuccore&id=";
$id = "";
$retmode = "&retmode=text";
$ua = LWP::UserAgent->new(timeout => 20);

while($row = <$gi>){
	chomp($row);
	$id = $id . $row . ",";
	if($. % 100 == 0){
		chop($id);
		$url = $base . $db . $id . $retmode;
		$id = "";
		$res = $ua->get($url);
		if($res->is_success()){
			print($res->decoded_content);
		}
		else {
			print STDERR $res->status_line;
		}
		print STDERR $. . "\n";
		sleep(3);
	}
}

close($gi);
