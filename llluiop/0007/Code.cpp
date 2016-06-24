#include "stdafx.h"
#include "CoreHook_Unity.h"
#include <TlHelp32.h>

using namespace CoreHook;

LPVOID Unity::GetVirtualCall(LPVOID pObject, int nIndex)
{
    if (NULL == pObject)
        return NULL;

    PDWORD_PTR pVirTable = (PDWORD_PTR)*(PDWORD_PTR)pObject;
    return (PDWORD_PTR)*(pVirTable + nIndex);
}

//test
LPVOID Unity::ScanCode(LPVOID pStart, DWORD dwLen, const BYTE pChar[], DWORD dwCharLen)
{
    if(!pStart || !dwLen || !dwCharLen)
    {
        return NULL;
    }
    DWORD i = 0;
    for(char * p = (char *)pStart; i < dwLen; i++, p++)
    {
        if(i + dwCharLen > dwLen)
        {
            break;
        }
        if(memcmp(p, pChar, dwCharLen) == 0)
        {
            return p;
        }
    }
    return NULL;
}

HMODULE Unity::GetModuleByPrefix( LPCWSTR lpPrefix )
{
    HMODULE hModule = NULL;
    HANDLE hSnapShot = CreateToolhelp32Snapshot(TH32CS_SNAPMODULE, 0);
    if (INVALID_HANDLE_VALUE != hSnapShot)
    { 
        MODULEENTRY32* moduleInfo = new MODULEENTRY32;
        moduleInfo->dwSize = sizeof(MODULEENTRY32);

        while (Module32Next(hSnapShot, moduleInfo) != FALSE)
        {
            std::wstring s = moduleInfo->szModule;
            if(-1 != s.find(lpPrefix))
            {
                hModule = moduleInfo->hModule;
                break;
            }

        }

        CloseHandle(hSnapShot);
        delete moduleInfo;
    }

    return hModule;
}

/*test*/
WORD Unity::FileMachineType( LPCTSTR lpExecuteFile )
{
    FILE *pfile = _tfopen(lpExecuteFile, L"rb");
    if (NULL == pfile)
        return (WORD)(0);

    IMAGE_DOS_HEADER idh;
    fread(&idh, sizeof(idh), 1, pfile);

    IMAGE_FILE_HEADER ifh;
    fseek(pfile, idh.e_lfanew + 4, SEEK_SET);
    fread(&ifh, sizeof(ifh), 1, pfile);
    fclose(pfile);

    return ifh.Machine;
}

CString Unity::GetFileNameByFullPath(LPCTSTR lpFileFullPath)
{
    TCHAR szPath[MAX_PATH] = {0};

    lstrcpyn(szPath, lpFileFullPath, Tsizeof(szPath));
    PathStripPath(szPath);

    return szPath;
}


BOOL Unity::ExeIsWebBrowser(LPCTSTR szExeFileName)
{
    if(lstrcmpi(szExeFileName, _T("iexplore.exe")) == 0
        || lstrcmpi(szExeFileName, _T("firefox.exe")) == 0
        || lstrcmpi(szExeFileName, _T("chrome.exe")) == 0
        || lstrcmpi(szExeFileName, _T("opera.exe")) == 0
        || lstrcmpi(szExeFileName, _T("Safari.exe")) == 0
        || lstrcmpi(szExeFileName, _T("dxsetup.exe")) == 0)

    {
        return TRUE;
    }
    return FALSE;
}

CString Unity::GetCreateProcessFileFullPath( LPCTSTR szApplicationName, LPCTSTR szCommandLine )
{
    TCHAR szPath[MAX_PATH] = {0};
    if(szApplicationName)
    {
        lstrcpyn(szPath, szApplicationName, Tsizeof(szPath));
    }
    else if(szCommandLine[0] == _T('\"'))
    {
        int nFind = 1;
        for(; szCommandLine[nFind] && szCommandLine[nFind] != _T('\"'); nFind++);
        lstrcpyn(szPath, &szCommandLine[1], nFind);
    }
    return szPath;
}

CString Unity::GetCreateProcessFileName( LPCTSTR szApplicationName, LPCTSTR szCommandLine )
{
    return GetFileNameByFullPath(GetCreateProcessFileFullPath(szApplicationName, szCommandLine));   
}


bool CoreHook::Unity::IsWindowsVersionOrGreater( WORD wMajorVersion, WORD wMinorVersion, WORD wServicePackMajor )
{
    
    OSVERSIONINFOEXW osvi = { sizeof(osvi), 0, 0, 0, 0, {0}, 0, 0 };
    DWORDLONG        const dwlConditionMask = VerSetConditionMask(
        VerSetConditionMask(
        VerSetConditionMask(
        0, VER_MAJORVERSION, VER_GREATER_EQUAL),
        VER_MINORVERSION, VER_GREATER_EQUAL),
        VER_SERVICEPACKMAJOR, VER_GREATER_EQUAL);

    osvi.dwMajorVersion = wMajorVersion;
    osvi.dwMinorVersion = wMinorVersion;
    osvi.wServicePackMajor = wServicePackMajor;

    return VerifyVersionInfoW(&osvi, VER_MAJORVERSION | VER_MINORVERSION | VER_SERVICEPACKMAJOR, dwlConditionMask) != FALSE;
    
}

CString CoreHook::Unity::GetCurModuelName()
{
    TCHAR szName[MAX_PATH]={0};
    GetModuleFileName(NULL,szName,MAX_PATH);
    PathStripPath(szName);

    return szName;
}