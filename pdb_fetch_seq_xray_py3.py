## What it does: Finds all PDBs with 95% sequence id to P00698 UAC (Hen egg white lysozyme) that have been resolved using X-RAY.
## From: http://www.rcsb.org/pages/webservices/python3_search_nmr and murpholinox@gmail.com
## Usage: `python thisfile`
## Output: the list of PDB IDs that conform to the search criteria.
## Works with: python3

import requests

if __name__ == '__main__':
    url = 'http://www.rcsb.org/pdb/rest/search'

    query_text = """
<orgPdbCompositeQuery version="1.0">
 <queryRefinement>
  <queryRefinementLevel>0</queryRefinementLevel>
  <orgPdbQuery>
    <version>head</version>
    <queryType>org.pdb.query.simple.SequenceQuery</queryType>
    <description>SEQUENCE P00698</description>
    <sequence>KVFGRCELAAAMKRHGLDNYRGYSLGNWVCAAKFESNFNTQATNRNTDGSTDYGILQINSRWWCNDGRTPGSRNLCNIPCSALLSSDITASVNCAKKIVSDGNGMNAWVAWRNRCKGTDVQAWIRGCRL</sequence>
    <searchTool>psiblast</searchTool>
    <maskLowComplexity>yes</maskLowComplexity>
    <eValueCutoff>10.0</eValueCutoff>
    <sequenceIdentityCutoff>95</sequenceIdentityCutoff>
  </orgPdbQuery>
 </queryRefinement>
 <queryRefinement>
  <queryRefinementLevel>1</queryRefinementLevel>
  <conjunctionType>and</conjunctionType>
  <orgPdbQuery>
    <version>head</version>
    <queryType>org.pdb.query.simple.ExpTypeQuery</queryType>
    <description>X-RAY with Data</description>
    <mvStructure.expMethod.value>X-RAY</mvStructure.expMethod.value>
    <mvStructure.hasExperimentalData.value>Y</mvStructure.hasExperimentalData.value>
  </orgPdbQuery>
 </queryRefinement>
</orgPdbCompositeQuery>

"""

    print("Query: %s" % query_text)
    print("Querying RCSB PDB REST API...")

    header = {'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.post(url, data=query_text, headers=header)

    if response.status_code == 200:
        print("Found %d PDB entries matching query." % len(response.text))
        print("Matches: \n%s" % response.text)
    else:
        print("Failed to retrieve results")



