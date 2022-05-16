## What it does: Finds all PDBs for a list of UACs
## From: https://www.uniprot.org/help/api_batch_retrieval then click on perl example
## Usage: `perl ./uniprot_batch_retrieval.pl` 
## Output: All possible information for given UACs 
## Works with: perl5

use strict;
use warnings;
use LWP::UserAgent;

my $list = $ARGV[0]; # File containg list of UniProt identifiers.

my $base = 'https://www.uniprot.org';
my $tool = 'uploadlists';

my $contact = ''; # Please set a contact email address here to help us debug in case of problems (see https://www.uniprot.org/help/privacy).
my $agent = LWP::UserAgent->new(agent => "libwww-perl $contact");
push @{$agent->requests_redirectable}, 'POST';

my $response = $agent->post("$base/$tool/",
                            [ 'file' => [$list],
                              'format' => 'txt',
                              'from' => 'ACC+ID',
                              'to' => 'ACC',
                              # If you want tab-separated output instead of full entries, specify 'tab' instead of 'txt' above
                              # and include the following optional line to include your preferred set of columns
                              # instead of the default from-to output:
                              'columns' => 'id,entry name,reviewed,protein names,genes,organism,length,database(RefSeq),go(molecular function)',

                            ],
                            'Content_Type' => 'form-data');

while (my $wait = $response->header('Retry-After')) {
  print STDERR "Waiting ($wait)...\n";
  sleep $wait;
  $response = $agent->get($response->base);
}

$response->is_success ?
  print $response->content :
  die 'Failed, got ' . $response->status_line .
    ' for ' . $response->request->uri . "\n";
