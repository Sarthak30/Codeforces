#include<bits/stdc++.h>
using namespace std;
map<int,int> m;
struct trie
{
    struct trie *child[2];
    bool isLeaf;
};
struct trie *getNode()
{
    struct trie *temp=(struct trie *)malloc(sizeof(struct trie));
    temp->isLeaf=false;
    temp->child[0]=NULL;
    temp->child[1]=NULL;
    return temp;
}
void getBin(int num,int arr[])
{
    for(int i=0;i<32;++i)
    {
        int k=(1<<i);
        if(k&num)
            arr[31-i]=1;
        else
            arr[31-i]=0;
    }
}
void insertTrie(int arr[],trie *root)
{
    trie *crawl=root;
    for(int i=0;i<32;++i)
    {
        if(crawl->child[arr[i]])
            crawl=crawl->child[arr[i]];
        else
        {
            crawl->child[arr[i]]=getNode();
            crawl=crawl->child[arr[i]];
        }
    }
    crawl->isLeaf=true;
}
bool isItFreeNode(trie *root)
{
    for(int i=0;i<2;++i)
        if(root->child[i])
            return false;
    return true;
}
bool isItLeafNode(trie *root)
{
    return root->isLeaf;
}
bool deleteTrie(int arr[],trie *root,int idx,int level)
{
    if(root)
    {
        if(idx==level)
        {
            if(root->isLeaf==true)
            {
                root->isLeaf=false;
                if(isItFreeNode(root)==true)
                    return true;
                else
                    return false;
            }
        }
        else
        {
            if(deleteTrie(arr,root->child[arr[idx]],idx+1,level))
            {
                free(root->child[arr[idx]]);
                root->child[arr[idx]]=NULL;
                return (isItFreeNode(root) && !isItLeafNode(root));
            }
        }
    }
    return false;
}
bool trie_search(int arr[],trie *root)
{
    trie *crawl=root;
    for(int i=0;i<32;++i)
    {
        if(crawl->child[arr[i]])
            crawl=crawl->child[arr[i]];
        else
            return false;
    }
    if(crawl->isLeaf==true)

        return true;
    else
        return false;
}
int maxi(int arr[],trie * root)
{
    trie *crawl=root;
    int ans=0;
    for(int i=0;i<32;++i)
    {
        int wanted=1-arr[i];
        if(crawl->child[wanted])
        {
            ans=ans*2+1;
            crawl=crawl->child[wanted];
        }
        else if(crawl->child[arr[i]])
        {
            ans=ans*2;
            crawl=crawl->child[arr[i]];
        }
        else
            return -1e9;
    }
    return ans;
}
int main(void)
{
    freopen("in.txt","r",stdin);
    int arr[32];
    struct trie *root=getNode();
    int q;
    cin>>q;
    while(q--)
    {
        string temp;
        int num;
        cin>>temp>>num;
        if(temp[0]=='+')
        {
            m[num]++;
            if(m[num]==1)
            {
                getBin(num,arr);
                insertTrie(arr,root);
            }
        }
        else if(temp[0]=='-')
        {
            m[num]--;
            if(m[num]==0)
            {
                getBin(num,arr);
                deleteTrie(arr,root,0,32);
            }
        }
        else
        {
            getBin(num,arr);
            cout<<max(num,maxi(arr,root))<<endl;
        }
    }
    return 0;
}
