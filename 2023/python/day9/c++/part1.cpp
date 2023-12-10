#include "readlines.hpp"

std::vector<int> convertToIntVec( std::string line );

int computeNextIntInSequence( std::vector<int>& seq );

bool checkSeqAllZeros( std::vector<int>& seq );

std::vector<int> computeDiffVec( std::vector<int>& input );

int main( int argc, char* argv[0]) 
{

    std::vector< std::string > lines;

    std::vector< std::vector<int> > lineVec;
    
    if( argc == 2 )
    {
        lines = readLines( argv[1] );


        for( std::string& s : lines )
        {
            lineVec.push_back( convertToIntVec( s ) );
        }
    }


    int sum(0); 
    for( std::vector<int>& line : lineVec )
    {
        sum += computeNextIntInSequence( line );
    }

    std::printf("Sum of Histories: %d\n", sum);

    return(0);
}


std::vector<int> convertToIntVec( std::string line )
{

    std::vector<int> intVec;
    std::regex delim(" ");

    std::sregex_token_iterator it(line.begin(),line.end(),delim, -1);
    std::sregex_token_iterator end;

    std::vector< std::string > splitStr(it,end);

    for( std::string& s : splitStr )
    {
        intVec.push_back( std::stoi(s) );
    }

    return( intVec );
}

int computeNextIntInSequence( std::vector<int>& seq )
{
    int nextInt = seq.back();

    std::vector<int> diffVec = seq;

    std::printf("\nComputing diffVec of\n");
    for( int i : seq )
    {
        std::printf("%d ", i);
    }

    std::printf("\n");

    while( checkSeqAllZeros( diffVec ) == false )
    {
        diffVec = computeDiffVec( diffVec );

        nextInt += diffVec.back();
    }

    return( nextInt );
}

bool checkSeqAllZeros( std::vector<int>& seq )
{
    for( int& i : seq )
    {
        if( i != 0 )
        {
            return( false );
        }
    }

    return( true );
}


std::vector<int> computeDiffVec( std::vector<int>& input)
{

    std::vector<int> diff;

    int curDiff = 0;
    for( int i = 0; i < input.size() - 1; i++ )
    {
        curDiff = input[i+1] - input[i];

        diff.push_back(curDiff);

        std::printf("%d ", curDiff);
    }

    std::printf("\n");
    return( diff );
}